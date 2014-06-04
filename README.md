Next Generation Sequencing Pipeline
=============

Author: Sergio Lois Olmo Ph.D
(sergio.lois@gmail.com)



LuskinExoVar: Whole EXOme Sequencing Pipeline for VARiant Identification
-------------





REQUIREMENTS
--------------
**Software Dependecies**
* BWA: Burrows-Wheeler Aligner
* SAMTOOLS
* Picard tools
* GATK: Genome Analysis ToolKit
* Java

**Biological data requirements**
* Reference genome
* Known collection of indels

COMMON ERRORS & SOLUTIONS
--------------
**Lexicographically sorted human genome sequence detected in reads**

The contig ordering in the reference you used must exactly match that of one of the official references canonical orderings. These are defined by historical karotyping of largest to smallest chromosomes, followed by the X, Y, and MT; the order is thus 1, 2, 3, ..., 10, 11, 12, ... 20, 21, 22, X, Y, MT. GATK will detect misordered contigs (for example, lexicographically sorted) and throw an error.

**Input files knownAlleles and reference have incompatible contigs: No overlapping contigs found.**

