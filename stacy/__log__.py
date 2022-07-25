
{'date': 'Mon Jul 25 2022 15:53:37.938 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 10
  for camara in tumba:
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Jul 25 2022 15:54:26.483 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 10
  for camara in tumba:
  ^
IndentationError: unexpected indent
'''},
{'date': 'Mon Jul 25 2022 15:56:27.260 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
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
  module <module> line 7
    tumba = lis("AMCDI"*3)
NameError: name 'lis' is not defined
'''},