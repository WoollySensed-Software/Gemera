# BOOT_LOADER = """
#     QWidget#BootLoaderUI {
#         background-color: #00008B;
#         color: white;
#     }
# """

# MAIN_WINDOW = """
#     QWidget#MainWindowUI {
#         background: #343434;
#         color: white;
#     }
#     QWidget#widget_top_bar_frame {
#         background: #28282B;
#         color: white;
#     }
#     QLabel#lbl_tb_title {
#         background: #28282B;
#         color: white;
#     }
#     QPushButton#top_bar_buttons {
#         background: #28282B;
#         color: #FF0000;
#         border-radius: 50%;
#     }
#     QPushButton#top_bar_buttons:hover{
#         background: rgba(0, 173, 255, 0.1);
#         border-radius: 50%;
#     }
#     QPushButton#top_bar_buttons:pressed{
#         background: rgba(0, 173, 255, 0.5);
#         border-radius: 50%;
#     }

#     QWidget#widget_central_area {
#         background: #343434;
#         color: white;
#     }
#     QLabel#lbl_modes_title {
#         background: #28282B;
#         color: white;
#         border-radius: 15%;
#     }

#     QRadioButton#rb_modes{
#         background: #343434;
#         color: white;
#     }
#     QRadioButton#rb_modes:hover{
#         background: rgba(255, 95, 31, 0.5);
#         border-radius: 10%;
#     }
#     QRadioButton#rb_modes:pressed{
#         background: #BF4717;
#         border-radius: 10%;
#     }
#     QRadioButton#rb_modes::checked{
#         background: #FF5F1F;
#         border-radius: 10%;
#     }
#     QRadioButton#rb_modes::indicator{
#         border: red;
#     }

#     QLabel#lbl_input_data_title {
#         background: #28282B;
#         color: white;
#         border-radius: 15%;
#     }
#     QLabel#lbl_input_data {
#         background: #343434;
#         color: white;
#     }
#     QLineEdit#ted_input_data {
#         background: #343434;
#         color: white;
#         border: 1px solid #343434;
#     }

#     QLabel#lbl_output_data_title {
#         background: #28282B;
#         color: white;
#         border-radius: 15%;
#     }
#     QLabel#lbl_output_data {
#         background: #343434;
#         color: white;
#     }
#     QLineEdit#ted_output_data {
#         background: #343434;
#         color: white;
#         border: 1px solid #343434;
#     }

#     QPushButton#btn_reset_pressure{
#         background: #FF5F1F;
#         color: white;
#         border: 1px solid #28282B;
#         border-radius: 45%;
#     }
#     QPushButton#btn_reset_pressure:hover{
#         background: #DF531B;
#     }
#     QPushButton#btn_reset_pressure:pressed{
#         background: #BF4717;
#     }

#     QPushButton#triple_buttons{
#         background: #FF5F1F;
#         color: white;
#         border: 1px solid #28282B;
#         border-radius: 50%;
#     }
#     QPushButton#triple_buttons:hover{
#         background: #DF531B;
#     }
#     QPushButton#triple_buttons:pressed{
#         background: #BF4717;
#     }

#     QWidget#widget_graph {
#         background: #28282B;
#     }
#     QWidget#widget_graph_frame {
#         background: white;
#     }

#     QWidget#widget_bottom_bar_frame {
#         background: #28282B;
#         color: white;
#     }

#     QPushButton#btn_open_close_com_port{
#         background: #28282B;
#         color: #FF0000;
#         border-radius: 10%;
#     }
#     QPushButton#btn_open_close_com_port:hover{
#         background: rgba(0, 173, 255, 0.1);
#         border-radius: 10%;
#     }
#     QPushButton#btn_open_close_com_port:pressed{
#         background: rgba(0, 173, 255, 0.5);
#         border-radius: 10%;
#     }

#     QPushButton#btn_open_weighers_menu{
#         background: #28282B;
#         color: #FF0000;
#         border-radius: 10%;
#     }
#     QPushButton#btn_open_weighers_menu:hover{
#         background: rgba(0, 173, 255, 0.1);
#         border-radius: 10%;
#     }
#     QPushButton#btn_open_weighers_menu:pressed{
#         background: rgba(0, 173, 255, 0.5);
#         border-radius: 10%;
#     }
#     QPushButton#btn_open_weighers_menu[enabled="false"] {color: gray;}
# """

# SETTINGS_WINDOW = """
#     QWidget#SettingsWindowUI {
#         background: #343434;
#         color: white;
#     }
#     QWidget#widget_top_bar_frame {
#         background: #28282B;
#         color: white;
#     }

#     QCheckBox#chb_use_weighers {
#         background: #343434;
#         color: white;
#     }
#     QCheckBox#chb_use_weighers::indicator {
#         background: 343434;
#         width: 30px;
#         height: 30px;
#     }
#     QCheckBox#chb_use_weighers::indicator:unchecked {
#         image: url(bin/resources/switch-off.png);
#     }
#     QCheckBox#chb_use_weighers::indicator:checked {
#         image: url(bin/resources/switch-on.png);
#     }

#     QLabel#labels_name {
#         background: #343434;
#         color: white;
#     }
#     QLabel#labels_name[enabled="false"] {color: gray;}

#     QComboBox#comboboxes {
#         background: #28282B;
#         color: white;
#         border: 1px solid #343434;
#     }
#     QComboBox#comboboxes:drop-down {
#         width: 0px;
#         height: 0px;
#         border: 0px;
#     }
#     QComboBox#comboboxes QAbstractItemView {
#         color: white;	
#         background-color: #28282B;
#         padding: 5px;
#     }
#     QComboBox#comboboxes QScrollBar {
#         width: 0px;
#         height: 0px;
#         border: 0px;
#     }
#     QComboBox#comboboxes[enabled="false"] {color: gray;}

#     QPushButton#btn_to_default {
#         background: #343434;
#         color: #FF0000;
#         border-radius: 15%;
#     }
#     QPushButton#btn_to_default:hover{
#         background: rgba(0, 173, 255, 0.1);
#     }
#     QPushButton#btn_to_default:pressed{
#         background: rgba(0, 173, 255, 0.5);
#     }

#     QPushButton#buttons {
#         background: #343434;
#         color: #FF0000;
#         border-radius: 15%;
#     }
#     QPushButton#buttons:hover{
#         background: rgba(0, 173, 255, 0.1);
#     }
#     QPushButton#buttons:pressed{
#         background: rgba(0, 173, 255, 0.5);
#     }

#     QMessageBox {
#         background: #28282B;
#         color: white;
#     }
#     QMessageBox QLabel{
#         background: #28282B;
#         color: white;
#     }

#     QMessageBox QPushButton{
#         background: #28282B;
#         color: #FF0000;
#         border-radius: 15%;
#     }
#     QMessageBox QPushButton:hover{
#         background: rgba(0, 173, 255, 0.1);
#     }
#     QMessageBox QPushButton:pressed{
#         background: rgba(0, 173, 255, 0.5);
#     }
# """

# WEIGHERS_WINDOW = """
#     QWidget#WeighersWindowUI {
#         background: #343434;
#         color: white;
#     }
#     QWidget#widget_top_bar_frame {
#         background: #28282B;
#         color: white;
#     }
#     QWidget#widget_central_area {
#         background: #343434;
#         color: white;
#     }

#     QLabel#lbl_tb_title {
#         background: #28282B;
#         color: white;
#     }

#     QPushButton#top_bar_buttons {
#         background: #28282B;
#         color: #FF0000;
#         border-radius: 50%;
#     }
#     QPushButton#top_bar_buttons:hover{
#         background: rgba(0, 173, 255, 0.1);
#         border-radius: 50%;
#     }
#     QPushButton#top_bar_buttons:pressed{
#         background: rgba(0, 173, 255, 0.5);
#         border-radius: 50%;
#     }

#     QComboBox#cb_command {
#         background: #28282B;
#         color: white;
#         border: 1px solid #343434;
#     }
#     QComboBox#cb_command:drop-down {
#         width: 0px;
#         height: 0px;
#         border: 0px;
#     }
#     QComboBox#cb_command QAbstractItemView {
#         color: white;	
#         background-color: #28282B;
#         padding: 5px;
#     }
#     QComboBox#cb_command QScrollBar {
#         width: 0px;
#         height: 0px;
#         border: 0px;
#     }

#     QPushButton#buttons {
#         background: #343434;
#         color: #FF0000;
#         border-radius: 15%;
#     }
#     QPushButton#buttons:hover{
#         background: rgba(0, 173, 255, 0.1);
#     }
#     QPushButton#buttons:pressed{
#         background: rgba(0, 173, 255, 0.5);
#     }
# """
