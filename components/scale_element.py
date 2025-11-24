import flet as ft

# A classe agora herda diretamente de ft.ExpansionTile
class ScaleListItem(ft.ExpansionTile):
    """
    Componente personalizado que representa uma Balança na lista, herdando 
    diretamente do ft.ExpansionTile para melhor encapsulamento.
    """
    def __init__(self, number: int, model: str, section: str, weight: int, **kwargs):
        
        # Armazenar dados da Balança no objeto
        self.scale_number = number
        self.scale_model = model
        self.scale_section = section
        self.scale_weight = weight
        
        # Propriedades de status (placeholders)
        self.measurement_date = None
        self.measured_by = None
        self.calibration_date = None
        self.calibrated_by = None
        self.clean_date = None
        self.cleaned_by = None

        # Chamar o construtor do pai (ft.ExpansionTile)
        # Toda a lógica de construção agora está aqui (antes estava em build())
        super().__init__(**kwargs)

        # 1. Lógica da Cor de Status
        color = ft.Colors.GREEN_700
        if self.scale_weight == 20000:
            color = ft.Colors.GREEN_700
        elif 19995 <= self.scale_weight <= 20005:
            color = ft.Colors.YELLOW_700
        else:
            color = ft.Colors.RED_700

        formatted_weight = f'{self.scale_weight:,.0f}'.replace(',', '.')

        # 2. Linha de Subtítulos (Modelo, Setor, Peso, Status)
        subtitles = ft.Row( 
            controls=[ 
                ft.Text(f'Modelo: {self.scale_model}', size=12, color=ft.Colors.GREY_600), 
                ft.Text(f'Setor: {self.scale_section}', size=12, color=ft.Colors.GREY_600), 
                ft.Text(f'Capacidade: {formatted_weight} Kg', size=12, color=ft.Colors.GREY_600),
                ft.Icon(ft.Icons.CHECK_CIRCLE, color=color, size=18, tooltip="Status de Aferição")
            ],
            spacing=15
        )

        # 3. Funções auxiliares (Definidas dentro do __init__ ou como métodos)
        def format_none(txt):
            """Formata valores None/vazios para 'N/A'."""
            return txt if txt else 'N/A'

        def delete_scale(e):
            # A remoção agora funciona da mesma forma, pois 'self' é o controlo
            # na lista de controlos do pai (ListView)
            if self.parent:
                self.parent.controls.remove(self)
                self.page.update()
                self.page.snack_bar = ft.SnackBar(ft.Text(f"Balança N° {self.scale_number} removida."), bgcolor=ft.Colors.RED_600)
                self.page.snack_bar.open = True
                self.page.update()

        # 4. Conteúdo Expandido
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

        # 5. Botões de Ação
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

        # 6. Atribuição das Propriedades do ExpansionTile (self)
        self.title = ft.Text(f'Balança: {self.scale_number}', weight=ft.FontWeight.BOLD)
        self.subtitle = subtitles
        self.controls = [last_measurement, last_calibration, last_clean, ft.Divider(), rw_buttons]
        self.controls_padding = ft.padding.only(left=20, bottom=10)
        self.collapsed_bgcolor = ft.Colors.WHITE
        self.bgcolor = ft.Colors.BLUE_GREY_50
        self.border_radius = ft.border_radius.all(8)