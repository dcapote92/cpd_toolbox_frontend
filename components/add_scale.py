import flet as ft
from components.scale_element import ScaleListItem 

class ScaleDialog(ft.AlertDialog):
    """
    Modal dialog to add a new scale
    """

    def __init__(self, page: ft.Page, listview_ref: ft.ListView, **kwargs):
        self.page = page
        self.listview_ref = listview_ref
        
        self.edt_numero = ft.TextField(
            label="Número",
            prefix_icon=ft.Icons.TAG, 
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=3,
            autofocus=True,
        )

        self.edt_modelo = ft.TextField(
            label="Modelo",
            prefix_icon=ft.Icons.DESCRIPTION,
            max_length=30,
            hint_text="Ex: Toledo 9091",
        )
        
        self.setores = ["Armazém A", "Linha de Produção 1", "Laboratório", "Expedição"]

        self.ddn_setor = ft.Dropdown(
            label="Setor",
            prefix_icon=ft.Icons.LOCATION_ON,
            options=[ft.dropdown.Option(setor) for setor in self.setores],
            hint_text="Selecione o setor onde a balança está localizada",
        )

        self.edt_peso = ft.TextField(
            label="Peso colhido (Kg)",
            prefix_icon=ft.Icons.LINE_WEIGHT,
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=6,
            hint_text="Ex: 20.000",
            suffix_text="Kg",
            on_change=self._format_weight_input
        )
        
        super().__init__(**kwargs)

        self.modal = True
        self.title = ft.Text("Adicionar Balança", weight=ft.FontWeight.BOLD)
        self.content = ft.Column(
            [
                self.edt_numero,
                self.edt_modelo,
                self.ddn_setor,
                self.edt_peso,
            ],
            tight=True, 
            spacing=20
        )
        self.actions = [
            ft.ElevatedButton(
                "Confirmar", 
                on_click=self._save_scale,
                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE)
            ),
            ft.TextButton(
                "Cancelar", 
                on_click=self._close_dialog,
                style=ft.ButtonStyle(bgcolor=ft.Colors.RED_600, color=ft.Colors.WHITE)
            )
        ]
        self.actions_alignment = ft.MainAxisAlignment.END
    
    def _format_weight_input(self, e: ft.ControlEvent):
        """Format weight input by adding a thousands separator every 3 digits"""

        raw_value = e.control.value.replace('.','').replace(',','')
        
        # exit on empty value
        if not raw_value:
            return
        
        try:
            # just checking its a number
            int(raw_value)
            number = raw_value.strip()
            
            if number.isdigit():
                number = str(int(number)) 
            
            formatted_number = '{:,}'.format(int(number)).replace(',','.')

            if e.control.value != formatted_number:
                e.control.value = formatted_number
                e.control.selection_base = len(formatted_number)
                e.control.selection_extent = len(formatted_number)
                e.control.update()
        except ValueError:
                pass

        


        
    
    def _close_dialog(self,e):
        self.snack_bar = ft.SnackBar(
            ft.Text('Ação cancelada!'),
            bgcolor=ft.Colors.YELLOW_700,
            duration=1500

        )
        self.page.close(self)
        self.page.open(self.snack_bar)
        self.page.update()

    def _save_scale(self, e):
        
        if not self.edt_numero.value or not self.ddn_setor.value:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, preencha o número e selecione o setor."),
                bgcolor=ft.Colors.RED_700
            )
            self.page.open(self.page.snack_bar)
            self.page.update()
            return

        try:
            numero = int(self.edt_numero.value)
            peso = int(float(self.edt_peso.value.replace('.', '').replace(',', '.'))) if self.edt_peso.value else 0 

        except ValueError:
            self.page.snack_bar = ft.SnackBar(
                ft.Text('Erro: Verifique se "Número" e "Capacidade Máxima" são números válidos.'),
                bgcolor=ft.Colors.RED_700
            )
            self.page.open(self.page.snack_bar)
            self.page.update()
            return
        
        new_item = ScaleListItem(
            number=numero,
            model=self.edt_modelo.value or "Desconhecido",
            section=self.ddn_setor.value or "Geral",
            weight=peso
        )
        
        self.listview_ref.controls.append(new_item)
        
        self.page.snack_bar = ft.SnackBar(
            ft.Text(f"Balança N° {numero} adicionada com sucesso!"),
            bgcolor=ft.Colors.GREEN_700
        )
        self.page.open(self.page.snack_bar)
        
        self._close_dialog(e)
        self.listview_ref.update() 
        
def scale_dialog(page: ft.Page, listview_ref: ft.ListView):
    dlg = ScaleDialog(page=page, listview_ref=listview_ref)
    page.dialog = dlg
    page.open(dlg)
    page.update()