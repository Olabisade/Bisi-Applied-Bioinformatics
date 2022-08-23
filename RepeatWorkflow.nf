nextflow.enable.dsl = 2

params.outdir = baseDir
params.tempdir = "${baseDir}/cache"

//This is a process for downloading a file
process downloadFile {
    storeDir "${params.tempdir}"
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    //publishDir "/home/cq/CQ/NGS", mode: 'copy', overwrite: true
    output:
        path "batch1.fasta"
        //path "batch1.fasta", emit: fasta
        //path "downloaddate.txt", emit: date
    """
    wget https://tinyurl.com/cqbatch1 -O batch1.fasta
    """
    //date > downloaddate.txt
}
process countSequences 
{
    //publishDir "/home/cq/CQ/NGS/", mode: 'copy', overwrite: true
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "numseqs.txt"
    """
    grep ">" ${infile}  | wc -l > numseqs.txt
    """
}
process splitSequences {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "sequence_*.fasta"
    """
    split -l 2 --additional-suffix .fasta -d ${infile} sequence_    
    """
}
process countBases {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path fastafile
    output:
        path "numbases.txt"
        //path "${fastafile.getSimpleName}_numbases.txt"
    """
    tail -1 ${fastafile} | wc -m > numbases.txt
    """
    //tail -1 ${fastafile} | wc -m > ${fastafile.getSimpleName}_numbases.txt 
}
process countRepeats {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path fastafile
    output:
        path "${fastafile.getSimpleName()}_numbRepeats.txt"
    """
    grep -o "GCCGCG" ${fastafile} | wc -l > ${fastafile.getSimpleName()}_numbRepeats.txt
    """
}

process collectResults 
{
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path textfiles
    output:
        path "summary.csv"
    """
    python ${baseDir}/collectResults.py *.txt > summary.csv
    """
}
workflow {
    fastafile = downloadFile()
    countSequences(fastafile)
    splitfastas = splitSequences(fastafile).view()
    splitfastas.flatten().view()
    countBases(splitfastas.flatten())
    repeats=countRepeats(splitfastas.flatten())
    repeats_collected = repeats.collect()
    repeats_collected.view()
    collectResults(repeats_collected)
    //collectResults(Channel.fromPath("*.txt")) 
}