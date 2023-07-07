def Tokenizer(model_name,**kwargs):
    if "wangchanberta-base-att-spm-uncased" in model_name:
        from .roberta import WangchanbertaTokenizer as tokenzer
    elif "wangchanberta-base-wiki-newmm" in model_name:
        from .core import ThaiWordsNewmmTokenizer as tokenzer
    elif "wangchanberta-base-wiki-syllable" in model_name:
        from .core import ThaiWordsSyllableTokenizer as tokenzer
    elif "wangchanberta-base-wiki-sefr" in model_name:
        from .core import FakeSefrCutTokenizer as tokenzer
    elif "wangchanberta-base-wiki-spm" in model_name:
        from .roberta import ThaiRobertaTokenizer as tokenzer
    else:
        from transformers import AutoTokenizer as tokenzer
    return tokenzer.from_pretrained(model_name,**kwargs)