import flet as ft

def add_listview_element(edt_num: ft.TextField, edt_model: ft.TextField, dropd_section: ft.Dropdown , edt_weight: ft.TextField, listview: ft.ListView, page: ft.Page, dialog: ft.AlertDialog):
    try:
        if not edt_num.value or not edt_weight.value:
            raise ValueError('Campos vazios')
        
        num = int(edt_num.value)
        weight = int(edt_weight.value)
        model = edt_model.value if edt_model.value else 'Desconhecido'
        section = dropd_section.value if dropd_section.value else 'Geral'

    except ValueError:
        page.snack_bar = ft.SnackBar(
            ft.Text('Erro: Verifique se "Número" e "Peso" são números válidos.'),
            bgcolor=ft.Colors.RED
            )
        page.snack_bar.open = True
        page.update()
        return


    color = ft.Colors.GREEN if weight == 20000 else (ft.Colors.YELLOW if 19995 <= weight <= 20005 else ft.Colors.RED )
    formatted_weight = f'{weight:,.0f}'.replace(',','.')

    def format_none(txt):
        return txt if txt else 'N/A'
    
    subtitles = ft.Row( 
        controls=[ 
            ft.Text(f'Modelo: {model}'), 
            ft.Text(f'Setor: {section}'), 
            ft.Text(f'Peso: {formatted_weight}'), # Usando formatado
            ft.Icon(ft.Icons.CHECK_CIRCLE, color=color)
        ],
        spacing=20
    )



    measurement_date = None
    measured_by = None
    calibration_date = None
    calibrated_by = None
    clean_date = None
    cleaned_by = None

       
    last_measurement = ft.Row(
        controls=[
            ft.Text(f'Última aferição: {format_none(measurement_date)}'),
            ft.Text(f'Responsável: {format_none(measured_by)}')
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    last_calibration = ft.Row(
        controls=[ 
            ft.Text(f'Última calibração: {format_none(calibration_date)}'),
            ft.Text(f'Responsável: {format_none(calibrated_by)}')
        ],
        alignment=ft.MainAxisAlignment.START
    )
    
    last_clean = ft.Row(
        controls=[ 
            ft.Text(f'Última limpeza: {format_none(clean_date)}'),
            ft.Text(f'Responsável: {format_none(cleaned_by)}')
        ],
        alignment=ft.MainAxisAlignment.START
    )


    btn_edit = ft.TextButton("Editar")
    btn_delete = ft.TextButton("Remover")

    rw_buttons = ft.Row(
        controls=[
            btn_edit,
            btn_delete
        ],
        alignment=ft.MainAxisAlignment.END
    )

    element = ft.ExpansionTile(
       title = ft.Text(f'Balança: {num}'),
       subtitle=subtitles,
       controls = [last_measurement, last_calibration, last_clean, rw_buttons]
    )

    listview.controls.append(element)

    edt_num.value = ""
    edt_model.value = ""
    dropd_section.value = None
    edt_weight.value = ""

    page.snack_bar = ft.SnackBar(ft.Text("Balança adicionada com sucesso!"), bgcolor=ft.Colors.GREEN)
    page.open(page.snack_bar)

    page.close(dialog)
    page.update()

def handle_search_update(search_term: str):
    pass