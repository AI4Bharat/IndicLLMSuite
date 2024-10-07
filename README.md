# IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages

🏆 ACL 2024 Outstanding Paper Award 🏆

This repository contains the artifacts and resources for curating Pre-training and Fine-tuning datasets for Indic Languages.

<p align="left">
  <a href="https://github.com/AI4Bharat/IndicLLMSuite/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green">
  </a>
  <a href="https://aclanthology.org/2024.acl-long.843/">
    <img src="https://img.shields.io/badge/ACL%20-2024-blue">
  </a>
</p>

![indicllmsuite-1](https://github.com/AI4Bharat/IndicLLMSuite/assets/31161768/f1a25b58-52f4-4544-ba36-8ebb8e2e01d5)

[📜 Paper](https://arxiv.org/abs/2403.06350) | [🌐 Blog](https://ai4bharat.iitm.ac.in) | [🤗 Data](https://huggingface.co/collections/ai4bharat/indicllmsuite-65ee7d225c337fcfa0991707)

IndicLLMSuite is the largest Pre-training and Instruction Fine-tuning dataset collection across 22 Indic languages. We open-source our pre-training dataset "Sangraha," the Instruction Fine-tuning dataset "IndicAlign-Instruct," and the Toxic alignment dataset "IndicAlign-Toxic." We also open-source all the code and other resources used for curating these datasets, including "Setu," a comprehensive data cleaning, filtering, and deduplication pipeline for Indic languages. We hope that this will advance the development of LLMs for Indian Languages.

We release the below Artifacts:

- [Sangraha](#sangraha)
- [IndicAlign](#indicalign)
  - [IndicAlign-Instruct](#indicalign-instruct)
  - [IndicAlign-Toxic](#indicalign-toxic)
- [Data Pipelines](#data-pipelines)
  - [Setu](#setu)
  - [Setu-translate](#setu-translate)
  - [Setu-transliterate](#setu-transliterate)
- [Other Resources](#other-resources)
  - [Portal for URL Verification](#portal-for-url-verification)
  - [Portal for Human Data Audit](#portal-for-human-data-audit)
  - [List of Toxic Words](#list-of-toxic-words)
  - [Romanization Dictionary](#romanization-dictionary)


## Sangraha
Sangraha is the largest high-quality, cleaned Indic language pretraining data containing 251B tokens summed up over 22 languages, extracted from curated sources, existing multilingual corpora, and large-scale translations. It has three broad components:
- **Sangraha Verified**: Contains scraped data from "human-verified" Websites, OCR-extracted data from high-quality Indic language PDFs, transcribed data from various Indic language videos, podcasts, movies, courses, etc. For scraping the data from the Web, we use the open-source framework [Webcorpus](https://github.com/AI4Bharat/webcorpus/tree/46af15a794fe101b0d9444f4a03dcd903be19fb7). For OCR, we collect PDFs from various sources with Internet Archive being the most prominent one. We release the code to download all the Indic Language PDFs from Internet Archive [here](https://github.com/AI4Bharat/sangraha-internet-archive-download/tree/94d32100b40f08450733895f9edb252d0590d9cb)
- **Sangraha Unverified**: High-quality Indic language data extracted from existing multilingual corpora. We employ perplexity filtering using n-gram language models trained on Sangraha Verified by extending the pipeline proposed by [CCNet](https://github.com/facebookresearch/cc_net/blob/main/cc_net/perplexity.py).
- **Sangraha Synthetic**: Wikimedia English translated to 14 Indic languages and further "romanized" from 14 languages by transliteration to English. We use the [Setu-translate](#setu-translate) and [Setu-transliterate](#setu-transliterate) pipelines for translation and transliteration, respectively.

Sangraha can be downloaded from [Huggingface 🤗](https://huggingface.co/datasets/ai4bharat/sangraha).

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

## IndicAlign
IndicAlign is the largest multilingual Instruction Fine-tuning dataset for Indic Languages, comprising a diverse collection of around 74.7 million prompt-response pairs. This data has been collected through four methods: aggregating existing Instruction Fine-tuning (IFT) datasets, translating high-quality English datasets to 14 Indic languages, generating synthetic data using context-grounded conversations from India-centric Wikipedia articles, and establishing a crowd-sourcing platform Anudesh for prompt collection. Indic Align comprises two distinct splits: [IndicAlign-Instruct](#indicalign-instruct) and [IndicAlign-Toxic](#indicalign-toxic).

IndicAlign can be downloaded from [Huggingface 🤗](https://huggingface.co/datasets/ai4bharat/indic-align).

### IndicAlign-Instruct
The IndicAlign-Instruct segment encompasses datasets that can be used to imbibe instruction-following ability in Large Language Models. It comprises of the below datasets:
- **IndicShareLlama**- Collection of first user prompts from [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered) along with responses from [Llama2-70B-Chat](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) model.
- **Dolly-T**- Translated and Romanised version of [Dolly-15K](https://huggingface.co/datasets/databricks/databricks-dolly-15k)
- **OpenAssistant-T**- Translated and Romanised version of [OpenAssistant v1](https://huggingface.co/datasets/OpenAssistant/oasst1)
- **WikiHow** - Translated and Romanised version of [WikiHow](https://huggingface.co/datasets/ai4bharat/indic-instruct-data-v0.1)
- **IndoWordNet**- Novel dataset created by converting the entried of [IndoWordNet](https://pypi.org/project/pyiwn/) to Instruction-Response pairs in 18 Indic languages.
- **Anudesh**- A crowd-sourced collection of prompts accompanied by responses generated from the Llama2-70B-Chat model.
- **Wiki-Conv**- Collection of short, to-the-point conversations on Wikipedia passages and Wiki-Infoboxes created using Llama2-70B-Chat model.
- **Wiki-Chat**- Collection of long, open conversations on Wikipedia passages created by simulating conversations between a User and an Assistant model.

### IndicAlign-Toxic
The IndicAlign-toxic segment encompasses datasets to align chat models to handle toxic prompts responsibly. It comprises of the below datasets:
- **HHRLHF-T**- Collection of "toxic" prompts from [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) with refusals from Llama2-70B-Chat model.
- **Toxic-Matrix**- A novel "synthetic" dataset with toxic prompts generated using [Mistral-7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) and non-toxic responses/refusals using Llama2-70B-Chat model.

For more details on Sangraha and IndicAlign, we direct the users towards our technical paper on [Arxiv](https://arxiv.org/abs/2403.06350). 


## Data Pipelines
We release the three data pipelines used for the curation of Sangraha. Setu (for data cleaning), Setu-translate (for large-scale translations), and Setu-transliterate (for large-scale transliterations).

### Setu
Setu is a comprehensive pipeline designed to clean, filter, and deduplicate diverse data sources, including Web, PDF, and Speech data. Built on Apache Spark, Setu encompasses four key stages: document preparation, document cleaning and analysis, flagging and filtering, and deduplication. Steps to setup and run Setu are available [here](https://github.com/AI4Bharat/setu/blob/main/README.md)

### Setu-translate
We release Setu-Translate, a pipeline for performing large-scale "structure-preserving" translations for both Pre-training and Conversation data. It is built on top of IndicTrans2 ([Gala et al., 2023](https://openreview.net/forum?id=vfT4YuzAYA)) and has three key stages: Templating, Inference, and Replace. Detailed instructions to set up and run Setu-translate are available [here](https://github.com/AI4Bharat/setu-translate/blob/master/README.md).

### Setu-transliterate
We also release Setu-transliterate, a pipeline for performing large-scale "structure-preserving" transliterations for Pre-training and Conversation data. Inherently, it uses IndicXlit ([Madhani et al., 2023](https://arxiv.org/abs/2205.03018)) but can consume any custom word mappings. Instructions for setting up and running Setu-transliterate are available [here](https://github.com/AI4Bharat/IndicLLMSuite/) [COMING SOON!!].

## Other Resources
Along with the main data and code artifacts, we release the other supplementary resources used at various stages in the curation of Sangraha and IndicAlign. We release these resources to foster open research.

### Portal for URL Verification
For curating Sangraha verified, we ensure that all the websites to be scraped are thoroughly verified by humans for quality. Websites containing toxic, adult, and poorly machine-translated content are discarded. We release the portal created for this human verification process. Steps to run this portal are available [here](https://github.com/AI4Bharat/IndicLLMSuite/tree/master/other_resources/url_verification).

### Portal for Human Data Audit
The data curated in Sangraha verified from both Web and PDFs is cleaned using the Setu data cleaning pipeline. We introduce another round of human audit after cleaning the data to verify the efficacy of the Setu Pipeline. We release the portal created for the human audit of both Web and PDF data. Steps to run this portal are available [here](https://github.com/AI4Bharat/IndicLLMSuite/tree/master/other_resources/human_audit).

### List of Toxic Words
We release the list of NSFW (Not Safe for Work) and toxic words across 17 Indic languages used to remove toxic content from the scraped data. The language-specific lists can be downloaded [here](https://github.com/AI4Bharat/setu/tree/main/setu/data/filter_data/nsfw).

### Romanization Dictionary
For performing large-scale transliterations, we first collect all the unique words present across Sangraha and IndicAlign and get their romanized versions using IndicXlit ([Madhani et al., 2023](https://arxiv.org/abs/2205.03018)). As a result, we create a massive dictionary of (word-romanized_Word) mapping for 14 Indic languages. We release the language-wise dictionary for direct future consumption. [COMING SOON!!!]


## Cite our Work

```
@article{khan2024indicllmsuite,
  title   = {IndicLLMSuite: A Blueprint for Creating Pre-training and Fine-Tuning Datasets for Indian Languages},
  author  = {Mohammed Safi Ur Rahman Khan and Priyam Mehta and Ananth Sankar and Umashankar Kumaravelan and Sumanth Doddapaneni and Suriyaprasaad G and Varun Balan G and Sparsh Jain and Anoop Kunchukuttan and Pratyush Kumar and Raj Dabre and Mitesh M. Khapra},
  year    = {2024},
  journal = {arXiv preprint arXiv: 2403.06350}
}
```


