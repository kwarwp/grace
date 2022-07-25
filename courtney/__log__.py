
{'date': 'Mon Jul 25 2022 15:37:37.73 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  input('Que legal, eu também')
  ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Jul 25 2022 15:37:54.731 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 4
    if perguntar == 'Sim':
NameError: name 'perguntar' is not defined
'''},
{'date': 'Mon Jul 25 2022 15:46:04.93 GMt-0300 (Hora padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  for camara in tumba:
  ^
IndentationError: unexpected indent
'''},