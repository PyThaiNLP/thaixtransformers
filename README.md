# ThaiXtransformers

Google colab: [Click](https://colab.research.google.com/github/PyThaiNLP/thaixtransformers/blob/main/notebooks/wangchanberta_getting_started_aireseach.ipynb)


Use Pretraining RoBERTa based Thai language models from VISTEC-depa AI Research Institute of Thailand.

Fork from [vistec-AI/thai2transformers](https://github.com/vistec-AI/thai2transformers).


This project build the tokenizer and preprocessing data for RoBERTa models from VISTEC-depa AI Research Institute of Thailand.

Paper: [WangchanBERTa: Pretraining transformer-based Thai Language Models](https://arxiv.org/abs/2101.09635)


## Install

> pip install thaixtransformers

## Uages

### Tokenizer

> from thaixtransformers import Tokenizer

If you use models, you should load model by model name.

> Tokenizer(model_name) -> Tokeinzer

**Example**

```python
from thaixtransformers import Tokenizer
from transformers import pipeline
from transformers import AutoModelForMaskedLM

tokenizer = Tokenizer("airesearch/wangchanberta-base-wiki-newmm")
model = AutoModelForMaskedLM.from_pretrained("airesearch/wangchanberta-base-wiki-newmm")

classifier = pipeline("fill-mask",model=model,tokenizer=tokenizer)
print(classifier("ผมชอบ<mask>มาก ๆ"))
# output:
#    [{'score': 0.05261131376028061,
#  'token': 6052,
#  'token_str': 'อินเทอร์เน็ต',
#  'sequence': 'ผมชอบอินเทอร์เน็ตมากๆ'},
# {'score': 0.03980604186654091,
#  'token': 11893,
#  'token_str': 'อ่านหนังสือ',
#  'sequence': 'ผมชอบอ่านหนังสือมากๆ'},
#    ...]
```

### Preprocess

If you want to preprocessing data before training model, you can use preprocess.

> from thaixtransformers.preprocess import process_transformers

> process_transformers(str) -> str

**Example**

```python
from thaixtransformers.preprocess import process_transformers

print(process_transformers("สวัสดี   :D"))
# output: 'สวัสดี<_>:d'
```


## BibTeX entry and citation info

```
@misc{lowphansirikul2021wangchanberta,
      title={WangchanBERTa: Pretraining transformer-based Thai Language Models}, 
      author={Lalita Lowphansirikul and Charin Polpanumas and Nawat Jantrakulchai and Sarana Nutanong},
      year={2021},
      eprint={2101.09635},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```