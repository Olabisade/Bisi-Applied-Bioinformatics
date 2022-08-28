nextflow.enable.dsl = 2

params.outdir = baseDir
params.tempdir = "${baseDir}/cache"

process downloadFile {
    storeDir "${params.tempdir}"
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    output:
        path "sequences.sam"
    """
    wget "https://gitlab.com/dabrowskiw/cq-examples/-/raw/master/data/sequences.sam?inline=false" -O sequences.sam
    """
}
process removeHeader {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "sequences.txt"
    """
    cat sequences.sam | grep -v "^@" > sequences.txt
    """
}
process removeGabbages {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "clean_sequence.txt"
    """
    cat sequences.txt | cut -f 1,10 --output-delimiter "," > clean_sequence.txt
    """
}
process realFormat {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "realFormat.txt"
    """
    cat clean_sequence.txt | sed -e 's/^/>/' > realFormat.txt
    """
}
process addFasta {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "sequences.fasta"
    """
    cat realFormat.txt | tr -s ',', '\n' > sequences.fasta
    """
}
process splitFasta {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path infile
    output:
        path "sequence_*.fasta"
    """
    split -l 2 -d --additional-suffix ".fasta" sequences.fasta sequence_ 
    """
}
process countStartCodons {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path fastafile
    output:
        path "${fastafile.getSimpleName()}_numbStartCodon.txt"
    """
    grep -o "ATG" ${fastafile} | wc -l > ${fastafile.getSimpleName()}_numbStartCodon.txt
    """
    //tail -1 | grep -o "ATG" | wc -l > ${fastafile.getSimpleName()}_numbStartCodon.txt
}
process countStopCodons {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path fastafile
    output:
        path "${fastafile.getSimpleName()}_numbStopCodon.txt"
    """
    grep -o "TAA" ${fastafile} | wc -l > ${fastafile.getSimpleName()}_numbStopCodon.txt
    """
}
process collectCodonResults 
{
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path textfiles
        path textfiles2
    output:
        path "*.csv"
    """
    python ${baseDir}/collectCodonResults.py *_numbStartCodon.txt *_numbStopCodon.txt > summaryCodons.csv
    """
}
workflow
{
    sequences = downloadFile()
    headerRemoved = removeHeader(sequences)
    gabbageRemoved = removeGabbages(headerRemoved)
    formatReal = realFormat(gabbageRemoved)
    fastaAdded = addFasta(formatReal)
    fastaSplit = splitFasta(fastaAdded)
    fastaSplit.flatten()
    startCodons = countStartCodons(fastaSplit.flatten())
    stopCodons = countStopCodons(fastaSplit.flatten())
    startCodons_collected = startCodons.collect()
    stopCodons_collected = stopCodons.collect()
    collectCodonResults(startCodons_collected, stopCodons_collected)
}