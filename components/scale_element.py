import flet as ft

class ScaleListItem(ft.ExpansionTile):
    """Custom scale item"""

    def __init__(self, number: int, model: str, section: str, weight: int, **kwargs):
        
        self.scale_number = number
        self.scale_model = model
        self.scale_section = section
        self.scale_weight = weight
        
        self.measurement_date = None
        self.measured_by = None
        self.calibration_date = None
        self.calibrated_by = None
        self.clean_date = None
        self.cleaned_by = None

        scale_title =ft.Text(f'Balança: {self.scale_number}', weight=ft.FontWeight.BOLD)

        super().__init__(title=scale_title, **kwargs)

        color = ft.Colors.GREEN_700
        if self.scale_weight == 20000:
            color = ft.Colors.GREEN_700
        elif 19995 <= self.scale_weight <= 20005:
            color = ft.Colors.YELLOW_700
        else:
            color = ft.Colors.RED_700

        formatted_weight = f'{self.scale_weight:,.0f}'.replace(',', '.')

        subtitles = ft.Row( 
            controls=[ 
                ft.Text(f'Modelo: {self.scale_model}', size=12, color=ft.Colors.GREY_600), 
                ft.Text(f'Setor: {self.scale_section}', size=12, color=ft.Colors.GREY_600), 
                ft.Text(f'Ultimo peso colhido: {formatted_weight} Kg', size=12, color=ft.Colors.GREY_600),
                ft.Icon(ft.Icons.CHECK_CIRCLE, color=color, size=18, tooltip="Status de Aferição")
            ],
            spacing=15
        )

        def format_none(txt):
            """Format None/empty values to 'N/A'."""
            return txt if txt else 'N/A'

        def delete_scale(e):
            if self.parent:
                snack_bar = ft.SnackBar(ft.Text(f"Balança N° {self.scale_number} removida."), bgcolor=ft.Colors.RED_600)
                self.parent.controls.remove(self)
                self.page.open(snack_bar)
                self.page.update()

        last_measurement = ft.Row(
            controls=[
                ft.Text(f'Última aferição: {format_none(self.measurement_date)}'),
                ft.Text(f'Responsável: {format_none(self.measured_by)}')
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=30
        )

        last_calibration = ft.Row(
            controls=[ 
                ft.Text(f'Última calibração: {format_none(self.calibration_date)}'),
                ft.Text(f'Responsável: {format_none(self.calibrated_by)}')
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=30
        )
        
        last_clean = ft.Row(
            controls=[ 
                ft.Text(f'Última limpeza: {format_none(self.clean_date)}'),
                ft.Text(f'Responsável: {format_none(self.cleaned_by)}')
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=30
        )

        btn_edit = ft.TextButton("Editar", icon=ft.Icons.EDIT, icon_color=ft.Colors.BLUE_600)
        btn_delete = ft.TextButton("Remover", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_600, on_click=delete_scale)

        rw_buttons = ft.Row(
            controls=[
                btn_edit,
                btn_delete
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=10
        )

        self.title = ft.Text(f'Balança: {self.scale_number}', weight=ft.FontWeight.BOLD)
        self.subtitle = subtitles
        self.controls = [last_measurement, last_calibration, last_clean, ft.Divider(), rw_buttons]
        self.controls_padding = ft.padding.only(left=20, bottom=10)
        self.collapsed_bgcolor = ft.Colors.WHITE
        self.bgcolor = ft.Colors.BLUE_GREY_50
        self.border_radius = ft.border_radius.all(8)