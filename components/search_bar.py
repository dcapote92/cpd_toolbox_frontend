import flet as ft

class SearchBar(ft.Container):
    def __init__(self, on_search=None, hint_text='Buscar...', **kwargs):
        super().__init__(**kwargs)
        
        self.on_search = on_search
        self.is_expanded = False
        self._is_focused = False  
        self._suppress_hover = False 

        self.padding = ft.padding.all(4)
        self.on_hover = self._handle_hover
        self.alignment = ft.alignment.center_right
        
        self.btn_search = ft.IconButton(
            icon=ft.Icons.SEARCH,
            tooltip='Buscar',
            on_click=lambda e: self._expand(with_focus=True)
        )

        self.edt_search = ft.TextField(
            keyboard_type=ft.KeyboardType.NUMBER,
            width=200,
            height=40,
            max_length=30,
            visible=False,
            hint_text=hint_text,
            prefix_icon=ft.Icons.SEARCH,
            on_focus=self._handle_focus, 
            on_blur=self._handle_blur,   
            on_change=self._handle_search_change,
            on_submit=self._handle_search_change
        )

        self.rw_organizer = ft.Row(
            controls=[
                self.btn_search,
                self.edt_search
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0
        )

        self.content = self.rw_organizer

    def _handle_search_change(self, e: ft.ControlEvent):
        search_term = e.control.value
        if self.on_search and callable(self.on_search):
            self.on_search(search_term)

    def _handle_focus(self, e: ft.ControlEvent):
        self._is_focused = True

    def _handle_hover(self, e: ft.ControlEvent):
        if e.data == 'true':
            if not self._suppress_hover:
                self._expand(with_focus=False)
        elif e.data == 'false':
            self._suppress_hover = False
            if not self._is_focused:
                self._collapse()
    
    def _handle_blur(self, e: ft.ControlEvent):
        self._is_focused = False
        self._suppress_hover = True 
        self._collapse()
    
    def _expand(self, e=None, with_focus=False):
        if not self.is_expanded:
            self.btn_search.visible = False
            self.edt_search.visible = True
            self.is_expanded = True
            self.update() 
            if with_focus:
                self.edt_search.focus()

    def _collapse(self):
        if self.is_expanded:
            self.edt_search.value = ''
            self.btn_search.visible = True
            self.edt_search.visible = False
            self.is_expanded = False
            self.update()