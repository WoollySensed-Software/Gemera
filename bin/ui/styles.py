BOOT_LOADER = """
    QWidget#BootLoaderUI {
        background-color: #00008B;
        color: white;
    }
"""

MAIN_WINDOW = """
    QWidget#MainWindowUI {
        background: #343434;
        color: white;
    }
    QWidget#widget_top_bar_frame {
        background: #28282B;
        color: white;
    }
    QLabel#lbl_tb_title {
        background: #28282B;
        color: white;
    }
    QPushButton#top_bar_buttons {
        background: #28282B;
        color: #FF0000;
        border-radius: 50%;
    }
    QPushButton#top_bar_buttons:hover{
        background: rgba(0, 173, 255, 0.1);
        border-radius: 50%;
    }
    QPushButton#top_bar_buttons:pressed{
        background: rgba(0, 173, 255, 0.5);
        border-radius: 50%;
    }

    QWidget#self.widget_central_area {
        background: #343434;
        color: white;
    }
    QLabel#lbl_modes_title {
        background: #28282B;
        color: white;
        border-radius: 15%;
    }

    QRadioButton#rb_modes{
        background: #343434;
        color: white;
    }
    QRadioButton#rb_modes:hover{
        background: rgba(255, 95, 31, 0.5);
        border-radius: 10%;
    }
    QRadioButton#rb_modes:pressed{
        background: #BF4717;
        border-radius: 10%;
    }
    QRadioButton#rb_modes::checked{
        background: #FF5F1F;
        border-radius: 10%;
    }
    QRadioButton#rb_modes::indicator{
        border: red;
    }

    QLabel#lbl_input_data_title {
        background: #28282B;
        color: white;
        border-radius: 15%;
    }
    QLabel#lbl_input_data {
        background: #343434;
        color: white;
    }
    QLineEdit#ted_input_data {
        background: #343434;
        color: white;
        border: 1px solid #343434;
    }

    QLabel#lbl_output_data_title {
        background: #28282B;
        color: white;
        border-radius: 15%;
    }
    QLabel#lbl_output_data {
        background: #343434;
        color: white;
    }
    QLineEdit#ted_output_data {
        background: #343434;
        color: white;
        border: 1px solid #343434;
    }

    QPushButton#btn_reset_pressure{
        background: #FF5F1F;
        color: white;
        border: 1px solid #28282B;
        border-radius: 45%;
    }
    QPushButton#btn_reset_pressure:hover{
        background: #DF531B;
    }
    QPushButton#btn_reset_pressure:pressed{
        background: #BF4717;
    }

    QPushButton#triple_buttons{
        background: #FF5F1F;
        color: white;
        border: 1px solid #28282B;
        border-radius: 50%;
    }
    QPushButton#triple_buttons:hover{
        background: #DF531B;
    }
    QPushButton#triple_buttons:pressed{
        background: #BF4717;
    }

    QWidget#widget_graph {
        background: #28282B;
    }
    QWidget#widget_graph_frame {
        background: white;
    }

    QWidget#widget_bottom_bar_frame {
        background: #28282B;
        color: white;
    }

    QPushButton#btn_open_close_com_port{
        background: #28282B;
        color: #FF0000;
        border-radius: 10%;
    }
    QPushButton#btn_open_close_com_port:hover{
        background: rgba(0, 173, 255, 0.1);
        border-radius: 10%;
    }
    QPushButton#btn_open_close_com_port:pressed{
        background: rgba(0, 173, 255, 0.5);
        border-radius: 10%;
    }

    QPushButton#btn_open_weigher_menu{
        background: #28282B;
        color: #FF0000;
        border-radius: 10%;
    }
    QPushButton#btn_open_weigher_menu:hover{
        background: rgba(0, 173, 255, 0.1);
        border-radius: 10%;
    }
    QPushButton#btn_open_weigher_menu:pressed{
        background: rgba(0, 173, 255, 0.5);
        border-radius: 10%;
    }
"""
