# IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages

This repository contains the artifacts and resources for curating Pre-training and Fine-tuning datasets for Indic Languages.

<p align="left">
  <a href="https://github.com/AI4Bharat/IndicLLMSuite/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green">
  </a>
</p>

![indicllmsuite-1](https://github.com/AI4Bharat/IndicLLMSuite/assets/31161768/f1a25b58-52f4-4544-ba36-8ebb8e2e01d5)

[📜 Paper](https://arxiv.org) | [🌐 Blog](https://ai4bharat.iitm.ac.in) | [🤗 Data](https://huggingface.co/collections/ai4bharat/indicllmsuite-65ee7d225c337fcfa0991707)

IndicLLMSuite is the largest Pre-training and Instruction Fine-tuning dataset collection across 22 Indic languages. We open-source our pre-training dataset "Sangraha," the Instruction Fine-tuning dataset "IndicAlign-Instruct," and the Toxic alignment dataset "IndicAlign-Toxic." We also open-source all the code and other resources used for curating these datasets, including "Setu," a comprehensive data cleaning, filtering, and deduplication pipeline for Indic languages. We hope that this will advance the development of LLMs for Indian Languages.

We release the below Artifacts:

- [Pre-training](#pre-training)
  - [Sangraha](#sangraha)
  - [Portal for URL Verification](#portal-for-url-verification)
  - [Portal for Human Data Audit](#portal-for-human-data-audit)
  - [List of Toxic Words](#list-of-toxic-words)
- [Instruction Fine-Tuning](#instruction-fine-tuning)
  - [IndicAlign](#indicalign)
  - [Romanization Dictionary](#romanization-dictionary)
  - [Toxic-Matrix Taxonomy](#toxic-matrix-taxonomy)
- [Data Pipelines](#data-pipelines)
  - [Setu](#setu)
  - [Setu-translate](#setu-translate)
  - [Setu-transliterate](#setu-transliterate)



## Pre-training

### Sangraha
Sangraha is the largest high-quality, cleaned Indic language pretraining data containing 251B tokens summed up over 22 languages, extracted from curated sources, existing multilingual corpora, and large-scale translations. It has three broad components:
- **Sangraha Verified**: Contains scraped data from "human-verified" Websites, OCR-extracted data from high-quality Indic language PDFs, transcribed data from various Indic language videos, podcasts, movies, courses, etc. For scraping the data from the Web, we use the open-source framework [Webcorpus](webcorpus_link). For OCR, we collect PDFs from various sources with Internet Archive being the most prominent one. We release pipeline to collect the Indic Language PDFs from Internet Archive [here](sangraha_download_link)
- **Sangraha Unverified**: High-quality Indic language data extracted from existing multilingual corpora. We employ perplexity filtering using n-gram language models trained on Sangraha Verified by extending the pipeline proposed by [CCNet](https://github.com/facebookresearch/cc_net/blob/main/cc_net/perplexity.py).
- **Sangraha Synthetic**: Wikimedia English translated to 14 Indic languages and further "romanized" from 14 languages by transliteration to English.

The list of languages in Sangraha:

<table>
<tbody>
  <tr>
    <td>Assamese (asm)</td>
    <td>Konkani (gom)</td>
    <td>Maithili (mai)</td>
    <td>Oriya (ori)</td>
    <td>Tamil (tam)</td>
    
  </tr>
  <tr>
    <td>Bengali (ben)</td>
    <td>Gujarati (guj)</td>
    <td>Malayalam (mal)</td>
    <td>Punjabi (pan)</td>
    <td>Telugu (tel)</td>
    
  </tr>
  <tr>
    <td>Bodo (brx)</td>
    <td>Hindi (hin)</td>
    <td>Marathi (mar)</td>
    <td>Sanskrit (san)</td>
    <td>Urdu (urd)</td>
  
  </tr>
  <tr>
    <td>Dogri (doi)</td>
    <td>Kannada (kan)</td>
    <td>Manipuri (mni)</td>
    <td>Santali (sat)</td>
 
  </tr>
  <tr>
    <td>English (eng)</td>
    <td>Kashmiri (kas)</td>
    <td>Nepali (nep)</td>
    <td>Sindhi (snd)</td>

  </tr>
  
</tbody>
</table>



### Portal for URL Verification
For curating Sangraha verified, we ensure that all the websites to be scraped are thoroughly verified by humans for quality. Websites containing toxic, adult, and poorly machine-translated content are discarded. We released the portal created for this human verification process. Steps to run this portal are available [here](#sangraha)

### Portal for Human Data Audit
The data curated in Sangraha verified from both Web and PDFs is cleaned using the Setu data cleaning pipeline. We introduce another round of human audit after cleaning the data to know the efficacy of the Setu Pipeline. We released the portal created for the human audit of both Web and PDF data. Steps to run this portal are available [here](#sangraha)

### List of Toxic Words
We release the list of NSFW (Not Safe for Work) and toxic words across 17 Indic languages to remove toxic content from the scraped data. The language-specific lists can be downloaded [here](https://github.com/AI4Bharat/setu/tree/main/setu/data/filter_data/nsfw)

## Data Pipelines
We release the three data pipelines used for the curation of Sangraha. Setu (for data cleaning), Setu-translate (for large-scale translations), and Setu-transliterate (for large-scale transliterations).

### Setu
Setu is a comprehensive pipeline designed to clean, filter, and deduplicate diverse data sources, including Web, PDF, and Speech data. Built on Apache Spark, Setu encompasses four key stages: document preparation, document cleaning and analysis, flagging and filtering, and deduplication. Steps to setup and run Setu are available [here](https://github.com/AI4Bharat/setu/blob/main/README.md)

### Setu-translate
We release Setu-Translate, a pipeline for performing large-scale "structure-preserving" translations for both Pre-training and Conversation 
