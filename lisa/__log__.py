
{'date': 'Mon Aug 29 2022 14:22:39.482 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  print a word 
        ^
SyntaxError: missing parenthesis in call to 'print'
'''},
{'date': 'Mon Aug 29 2022 14:22:53.955 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 4
  print ord(('g'))
        ^
SyntaxError: missing parenthesis in call to 'print'
'''},
{'date': 'Mon Aug 29 2022 14:23:08.412 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 4
  print (ord('g')
        ^
SyntaxError: Unbalanced bracket (
'''},
{'date': 'Mon Aug 29 2022 14:26:22.942 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''103
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 5
    print (ord('MSG')+2)
TypeError: ord() expected a character, but string of length 3 found
'''},