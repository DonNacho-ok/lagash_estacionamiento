#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Dec 08, 2019 06:39:26 PM -03  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 988x613+1629+173
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2951 870
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Gestion Estacionamiento"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab43 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab43" "Titulo_app" vTcl:WidgetProc "Toplevel1" 1
    listbox $top.lis44 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -height 516 -width 514 
    .top42.lis44 configure -font "TkFixedFont"
    .top42.lis44 insert end text
    vTcl:DefineAlias "$top.lis44" "Listbox" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab45" "search_label" vTcl:WidgetProc "Toplevel1" 1
    button $top.but46 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Button 
    vTcl:DefineAlias "$top.but46" "Ingress_button" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Button 
    vTcl:DefineAlias "$top.but47" "Egress_button" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent48 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$top.ent48" "Entry_add" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent49 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$top.ent49" "search_Entry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab52" "total_space_Label" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab53" "Free_space_Label" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab54" "Occu_Space_Label" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab55" "totals_Label" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab56 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab56" "frees_Label" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab57" "occus_Label" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text asdasd 
    vTcl:DefineAlias "$top.lab58" "Notif_space_Label" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab43 \
        -in $top -x 370 -y 10 -width 189 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lis44 \
        -in $top -x 460 -y 80 -width 514 -relwidth 0 -height 516 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 480 -y 40 -width 129 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 80 -y 70 -width 81 -relwidth 0 -height 51 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 80 -y 170 -width 81 -relwidth 0 -height 51 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 20 -y 130 -width 226 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 670 -y 40 -width 226 -relwidth 0 -height 33 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 20 -y 270 -width 159 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 20 -y 320 -width 159 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 30 -y 380 -width 139 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 240 -y 280 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 240 -y 330 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 240 -y 390 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 60 -y 470 -width 319 -relwidth 0 -height 61 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

