nextflow.enable.dsl = 2

params.outdir = "${baseDir}/out"
params.storedir = "${baseDir}/cache"
params.accession = "M21012"

process gb_downloadFile {
    storeDir params.storedir
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    output:
        path "${params.accession}.fasta"
    """
    wget "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=M21012&rettype=fasta&retmode=text" -O M21012.fasta
    """
}
process git_downloadFile {
    storeDir "${params.storedir}"
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    output:
        path ("*.fasta")
    """
    git clone https://gitlab.com/dabrowskiw/cq-examples.git
    cp cq-examples/data/hepatitis/seq*.fasta .
    """
}
process allFiles {
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path gbFasta
        path gitFasta
    output:
        path "allfiles.fasta"

    """
    cat ${gbFasta} > allfiles.fasta
    cat ${gitFasta} >> allfiles.fasta
    """
}
process mafftAligner {
    container "https://depot.galaxyproject.org/singularity/mafft%3A7.508--hec16e2b_0"
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path fastafile
    output:
        path "alligned_files.fasta"
    """
    mafft ${fastafile} > alligned_files.fasta
    """
}
process trimalAutomated {
    container "https://depot.galaxyproject.org/singularity/trimal%3A1.4.1--h9f5acd7_6"
    publishDir "${params.outdir}", mode: 'copy', overwrite: true
    input:
        path fastafile
    output:
        path "trimmed.fasta", emit: seqfile
        path "trimmed.html", emit: report_html
    """
    trimal -in ${fastafile} -out trimmed.fasta -htmlout trimmed.html -automated1
    """
}
workflow
{   
    gbFasta = gb_downloadFile()
    gitFasta = git_downloadFile()
    allFastafiles = allFiles(gbFasta, gitFasta)
    alligned_fasta = mafftAligner(allFastafiles)
    trimal_report = trimalAutomated(alligned_fasta)
}