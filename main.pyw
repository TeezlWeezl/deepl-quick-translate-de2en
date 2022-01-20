from deepl import Translator 
import win32clipboard as clp
import sys
import os

def translate_text(inp_text: str):
  trnsl = Translator(auth_key=os.environ.get('DEEPL_AUTH'))
  result = trnsl.translate_text(inp_text.replace('·', ' '), source_lang='DE', target_lang='EN-US')
  return result.text

clp.OpenClipboard()
clp.EmptyClipboard()
clp.SetClipboardText(translate_text(sys.argv[1]), clp.CF_TEXT)
clp.CloseClipboard()