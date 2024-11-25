style = '''
#centralwidget > QWidget {
    border-radius: 10px;
    background: #151515;
}

#centralwidget QWidget {
    background: #151515;
}



#topSpace {
    border-bottom: 1px solid #4F4F4F;
}

#close, #hide {
    background: #151515;
    padding: 0;
    border-radius: 0;
    margin: 0;
    border-bottom: 1px solid #4F4F4F;
    color: #818181;
}

#close:hover, #hide:hover {
    background: #4F4F4F;
    color: #151515;
}

#hide {
    background: #151515;
    border-left: 1px solid #4F4F4F;
}
#close {
    border-top-right-radius: 10px;
}


#bottomSpace {
    border-top: 1px solid #4F4F4F;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}



QMenu {
    background: #151515;
    border: 1px solid #4F4F4F;
    border-radius: 5px;
}
QMenu::item {
    color: #818181;
    padding: 5px 10px;
    border-bottom: 1px solid #4F4F4F;
}
QMenu::item:selected {
    background: #4F4F4F;
    color: #151515;
}
'''