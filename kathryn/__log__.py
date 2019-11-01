
{'date': 'Fri Nov 01 2019 13:59:10.518 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 3
  from _spy.vitollino.main import INVENTARIO INV
                                                ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Fri Nov 01 2019 13:59:47.66 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 6
    class brulu():
  module <module> line 7
    saku= Elemento(img=saku)
NameError: name 'saku' is not defined
'''},