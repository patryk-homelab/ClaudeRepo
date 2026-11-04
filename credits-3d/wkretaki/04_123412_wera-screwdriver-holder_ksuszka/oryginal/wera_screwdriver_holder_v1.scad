// Wall mounted holders for Wera screwdrivers
// Author: Krzysztof Suszka
// Last update: 2024-01-09

// Customizer variables
handle_diameter = 36; // [32, 34, 36, 40]
handle_bottom_outer_diameter = 26.7; // [17.2, 19.3, 23, 26.7, 31.2]
handle_bottom_inner_diameter = 23; // [15, 17, 21.5, 23, 26.4]
thin_shaft_diameter = 5.0; // [3:0.5:15]
thick_shaft_diameter = 5.0; // [3:0.5:15]
symbol = "tx"; // ["flat", "ph", "pz", "tx", "hex", "nut", "bottle_opener", "none"]
label_first_line = "TX";
label_second_line = "25";
handle_sides = 6; // [4,5,6,7,8,9,10,12,60]

// Uncomment/modify below part you want to render:

// Dimensions for some of Wera screwdrivers
// model - handle_length handle_dia handle_hex_dia, handle_bottom_hex_wide_dia handle_bottom_circle_dia shaft_dia
// model                   |  hl |  hd  | hexd | bhd  | hbcd | shaftd
// ------------------------+-----+------+------+------+------+----------
// 932 1.2x7.0             | 105 | 36   | 26.7 | 29.2 | 23   | 11.5/6.8
// 350 PH 2x100            | 105 | 36   | 26.7 | 29.2 | 23   | 6
// 350 PH 3                | 112 | ?    | 31.2 | ?    | 26.4 | 8    ???
// 367 TX 25               | 105 | 36   | 26.7 | 29.2 | 23   | 5
// 367 TX 20               |  98 | 32   | 23   | 25   | 21.5 | 4.5
// 367 TX 15               |  98 | 32   | 23   | 25   | 21.5 | 4
// 335 Flat 0.8x4.0x100    |  98 | 32   | 23   | 25   | 21.5 | 4
// 160i Flat 0.6x3.5x100   |  81 | 25.5 | 19.3 | 20.8 | 17   | 7
// 160i Flat 0.4x2.5x80    |  81 | 25.5 | 19.3 | 20.8 | 17   | 6
// 352 Hex 2               |  70 | ?    | 16.5 | ?    | 15   | 3    ???
// 247 Flat 0.5x3.0x70     |     | 23   | 17.1 | 19.1 | 14   | 8.4
// 932A Flat 12            | 117 |      |      |      |      |

module customizer_wera_holder() {
  wera_holder(handle_diameter,
    handle_bottom_outer_diameter,
    handle_bottom_inner_diameter,
    thin_shaft_diameter,
    thick_shaft_diameter,
    symbol,
    (label_second_line == "")? label_first_line: [label_first_line, label_second_line],
    handle_sides
  );
}

lineup() {
  // Customizer version
  customizer_wera_holder();

//wera_holder(32,23,21.5,5.0,5.0,"flat","5.0");     // 334 Flat 0.8x5.0
//wera_holder(36,26.7,23,6.0,6.0,"flat","6.0");     // 334 Flat 1.0x6.0
//wera_holder(36,26.7,23,6.0,6.0,"flat","6.5");     // 334 Flat 1.2x6.5x150
//wera_holder(36,26.7,23,7.0,7.0,"flat","6.5");     // 334 Flat 1.2x6.5x200
//wera_holder(36,26.7,23,7.0,7.0,"flat","7.0");     // 334 Flat 1.2x7.0
//wera_holder(40,31.2,26.4,8,8,"flat","8.0");       // 334 Flat 1.2x8.0
//wera_holder(40,31.2,26.4,10,10,"flat","10");       // 334 Flat 1.6x10.0

//wera_holder(32,17.2,15,3.5,3.5,"flat","2.5");     // 335 Flat 0.4x2.5
//wera_holder(32,19.3,17,4.0,4.0,"flat","3.0");     // 335 Flat 0.5x3.0
//wera_holder(32,19.3,17,3.5,3.5,"flat","3.5");     // 335 Flat 0.6x3.5
//wera_holder(32,23,21.5,4.0,4.0,"flat","4.0");     // 335 Flat 0.8x4.0
//wera_holder(32,23,21.5,5.5,5.5,"flat","5.5");     // 335 Flat 1.0x5.5
//wera_holder(32,24.5,23,5.5,5.5,"flat","5.5");     // 335 Flat 1.0x5.5 24mm
//wera_holder(36,26.7,23,6.0,6.0,"flat","6.0");     // 335 Flat 1.2x6.0

//wera_holder(32,19.3,17,6.0,6.0,"flat","2.5");     // 160i Flat 0.4x2.5
//wera_holder(33,19.3,17,7.0,7.0,"flat","3.5");     // 160i Flat 0.6x3.5
//wera_holder(34,23,21.5,7.0,7.0,"flat","4.0");     // 160iS Flat 0.8x4.0
//wera_holder(36,23,21.5,9.0,9.0,"flat","5.5");     // 160iS Flat 1x5.5
//wera_holder(33,17.2,15,7.6,7.6,"flat","3.0");     // 247 Flat 0.5x3.0
//wera_holder(32,19.3,17,6.0,6.0,"ph",["PH", "0"]);     // 162i PH 0
//wera_holder(34,23,21.5,7.0,7.0,"ph",["PH", "1"]);     // 162i PH 1
//wera_holder(36,26.7,23,9.0,9.0,"ph",["PH", "2"]);     // 162i PH 2
//wera_holder(40,31.2,26.4,12.0,12.0,"ph",["PH", "3"]); // 162i PH 3
//wera_holder(40,31.2,26.4,14.0,14.0,"ph",["PH", "4"]); // 162i PH 4
//wera_holder(34,23,21.5,7.0,7.0,"pz",["PZ", "1"]);     // 165i PZ 1
//wera_holder(36,26.7,23,9.0,9.0,"pz",["PZ", "2"]);     // 165i PZ 2
//wera_holder(34,23,21.5,7.0,7.0,"tx",["TX","20"]);     // 167i TX 20
//wera_holder(36,26.7,23,9.0,9.0,"tx",["TX","25"]);     // 167i TX 25


//wera_holder(32,19.3,17,3,3,"ph",["PH", "0"]);     // 350 PH 0
//wera_holder(32,23,21.5,4.5,4.5,"ph",["PH", "1"]); // 350 PH 1
//wera_holder(32,24.5,23,4.5,4.5,"ph",["PH", "1"]); // 350 PH 1 24mm
//wera_holder(36,26.7,23,6,6,"ph",["PH","2"]);      // 350 PH 2
//wera_holder(40,31.2,26.4,8,8,"ph",["PH","3"]);    // 350 PH 3
//wera_holder(40,31.2,26.4,10,10,"ph",["PH","4"]);  // 350 PH 4

//wera_holder(32,19.3,17,3,3,"pz",["PZ", "0"]);     // 355 PZ 0
//wera_holder(32,23,21.5,4.5,4.5,"pz",["PZ", "1"]); // 355 PZ 1
//wera_holder(36,26.7,23,6,6,"pz",["PZ","2"]);      // 355 PZ 2
//wera_holder(40,31.2,26.4,8,8,"pz",["PZ","3"]);    // 355 PZ 3
//wera_holder(40,31.2,26.4,10,10,"pz",["PZ","4"]);  // 355 PZ 4

//wera_holder(32,17.2,15,3.5,3.5,"tx",["TX","5"]);  // 367 TX 5
//wera_holder(32,17.2,15,3.5,3.5,"tx",["TX","6"]);  // 367 TX 6
//wera_holder(32,17.2,15,3.5,3.5,"tx",["TX","7"]);  // 367 TX 7
//wera_holder(32,19.3,17,3.5,3.5,"tx",["TX","8"]);  // 367 TX 8
//wera_holder(32,19.3,17,4.0,4.0,"tx",["TX","9"]);  // 367 TX 9
//wera_holder(32,19.3,17,4.0,4.0,"tx",["TX","10"]); // 367 TX 10
//wera_holder(32,23,21.5,4.0,4.0,"tx",["TX","15"]); // 367 TX 15
//wera_holder(32,23,21.5,4.5,4.5,"tx",["TX","20"]); // 367 TX 20
//wera_holder(36,26.7,23,5.0,5.0,"tx",["TX","25"]); // 367 TX 25
//wera_holder(36,26.7,23,5.5,5.5,"tx",["TX","27"]); // 367 TX 27
//wera_holder(36,26.7,23,6.0,6.0,"tx",["TX","30"]); // 367 TX 30
//wera_holder(40,31.2,26.4,7,7,"tx",["TX","40"]);   // 367 TX 40

//wera_holder(32,16.5,15,3.0,3.0,"hex","1.5");      // 352 1.5
//wera_holder(32,16.5,15,3.0,3.0,"hex","2");        // 352 2.0
//wera_holder(32,19.3,17,3.0,3.0,"hex","2.5");      // 352 2.5
//wera_holder(32,19.3,17,4.0,4.0,"hex","3");        // 352 3.0
//wera_holder(32,23,21.5,5.0,5.0,"hex","4");        // 352 4.0
//wera_holder(36,26.7,23,6.0,6.0,"hex","5");        // 352 5.0
//wera_holder(36,26.7,23,7.0,7.0,"hex","6");        // 352 6.0
//wera_holder(40,31.2,26.4,10,10,"hex","8");        // 352 8.0
//wera_holder(40,31.2,26.4,12,12,"hex","10");       // 352 10.0

// Dimensions provided by @Vimmelman_1386205
//wera_holder(38,23,21.5,12,12,"nut","6");          // 391 6.0
//wera_holder(38,23,21.5,12,12,"nut","7");          // 391 7.0
//wera_holder(38,23,21.5,12,12,"nut","8");          // 391 8.0

//wera_holder(40,23,21.5,11,11,"nut","¼\"");        // 393S

//wera_holder(34,23,21.5,7.2,7.2,"nut","5");        // 395 HO 5.0
//wera_holder(34,23,21.5,7.2,7.2,"nut","5.5");      // 395 HO 5.5
//wera_holder(34,23,21.5,7.2,7.2,"nut","6");        // 395 HO 6.0
//wera_holder(36,26.7,23,7.2,7.2,"nut","7");        // 395 HO 7.0
//wera_holder(36,26.7,23,9.3,9.3,"nut","8");        // 395 HO 8.0
//wera_holder(40,31.2,26.4,9.3,9.3,"nut","10");     // 395 HO 10.0
//wera_holder(40,31.2,26.4,11,11,"nut","13");       // 395 HO 13.0

//wera_holder(40,31.2,26.4,9,9,"nut","¼\"");        // 812/1

//wera_holder(36,23,21.5,6,9.5,"ph",["PH","1"]);    // 917 SPH PH 1
//wera_holder(36,26.7,23,7,11.5,"ph",["PH","2"]);   // 917 SPH PH 2
//wera_holder(40,31.2,26.4,9,14.5,"ph",["PH","3"]); // 917 SPH PH 3

//wera_holder(36,23,21.5,6,9.5,"pz",["PZ", "1"]);   // 918 SPZ PZ 1
//wera_holder(36,26.7,23,7,11.5,"pz",["PZ", "2"]);  // 918 SPZ PZ 2
//wera_holder(40,31.2,26.4,9,14.5,"pz",["PZ","3"]); // 918 SPZ PZ 3

//wera_holder(32,19.3,17,5.0,5.0,"flat","3.5");     // 932A Flat 0.6x3.5
//wera_holder(36,23,21.5,6,9.5,"flat","4.5");       // 932A Flat 0.8x4.5
//wera_holder(36,26.7,23,7,11.5,"flat","5.5");      // 932A Flat 1.0x5.5
//wera_holder(36,26.7,23,7,11.5,"flat","7.0");      // 932A Flat 1.2x7.0
//wera_holder(40,31.2,26.4,9,15,"flat","9.0");      // 932A Flat 1.6x9.0
//wera_holder(40,31.2,26.4,9,15,"flat","10");       // 932A Flat 1.6x10.0
//wera_holder(44,33,28,18.5,18.5,"flat","12");      // 932A Flat 2.0x12.0
//wera_holder(44,33,28,18.5,18.5,"flat","14");      // 932A Flat 2.5x14.0

//wera_holder(36,23,21.5,6,9.5,"tx",["TX","20"]);   // 977 TX 20
//wera_holder(36,26.7,23,7,11.5,"tx",["TX","25"]);  // 977 TX 25

//wera_bottle_opener_holder();

//rotate([0,0,90])spacer(5);

//wera_holder(36,22,20,10.0,10.0,"nut","¼″",12, main_font=[8,"Arial:style=Narrow","center","center"]);     // PB Swiss
//wera_holder(36,21,20,6.0,10.0,"nut","¼″",12, main_font=[8,"Arial:style=Narrow","center","center"]);     // PB Swiss 8451.10-100
//wera_holder(36,23.5,21,10.0,10.0,"nut","¼″",12, main_font=[8,"Arial:style=Narrow","center","center"]);     // PB 8453

//wera_holder(38,22.5,20,11.0,11.0,"nut","¼″",12, main_font=[8,"Arial:style=Narrow","center","center"]);  // Makita D-58833
//wera_holder(38,30.6,25,10.0,10.0,"nut","¼″",12, main_font=[8,"Arial:style=Narrow","center","center"]);  // Makita D-73221 Mini
}


//rail(25.4*8,25.4);
//rail(45*6,45);
//rail(40*6,40);
//rail_with_peg_holes(45*5);
//rail_peg_screw_4mm();
//rail_ikea_skadis(6);
//rail_inch_pegboard(8,board_thickness=0);

// https://www.printables.com/model/152592-honeycomb-storage-wall
//honeycomb_wall_spacing=40.88;
//rail(honeycomb_wall_spacing*6,honeycomb_wall_spacing);
//echo(honeycomb_wall_spacing*6);

// =============================================================================

FFF="FFF";FFT="FFT";FTF="FTF";FTT="FTT";TFF="TFF";TFT="TFT";TTF="TTF";TTT="TTT";
module cube2(size, center) {
  function centered(i)=center[i]=="T"||center[i]==true;
  translate([
    centered(0) ? -size[0]/2 : 0,
    centered(1) ? -size[1]/2 : 0,
    centered(2) ? -size[2]/2 : 0]) cube(size);
}
module cube_chamfered(size, center, chamfer=1) {
  function centered(i)=center[i]=="T"||center[i]==true;
  translate([
    centered(0) ? 0 : size[0]/2,
    centered(1) ? 0 : size[1]/2,
    centered(2) ? 0 : size[2]/2]) hull() {
      cube([size[0]-2*chamfer,size[1]-2*chamfer,size[2]],center=true);
      cube([size[0]-2*chamfer,size[1],size[2]-2*chamfer],center=true);
      cube([size[0],size[1]-2*chamfer,size[2]-2*chamfer],center=true);
    }
}
module copy_x() {
  for(a=[0,1])mirror([a,0,0])children();
}
module copy_y() {
  for(a=[0,1])mirror([0,a,0])children();
}
module copy_z() {
  for(a=[0,1])mirror([0,0,a])children();
}

module lineup(dy=30) {
  for(i=[0:1:$children-1])translate([0,dy*i])rotate([90,0])children(i);
}

module symbol(type) {
  module symbol_circle() {
    difference() {
      circle(d=10,$fn=48);
      circle(d=8,$fn=48);
    }
  }
  if (type=="flat") {
    symbol_circle();
    square([7,1.5],center=true);
  } else if (type == "ph") {
    symbol_circle();
    square([7,1.2],center=true);
    square([1.2,7],center=true);
  } else if (type == "pz") {
    symbol_circle();
    square([7,1.2],center=true);
    square([1.2,7],center=true);
    for(a=[45:90:160])rotate([0,0,a]) hull(){
      square([6,0.2],center=true);
      square([2,1],center=true);
    }
  } else if (type == "tx") {
    symbol_circle();
    for(a=[-30,30])rotate([0,0,a])circle(d=7,$fn=3);
  } else if (type == "hex") {
    symbol_circle();
    circle(d=6,$fn=6);
  } else if (type == "nut") {
    difference() {
      circle(d=10,$fn=48);
      circle(d=8,$fn=6);
    }
  } else if (type == "bottle_opener") {
    bottle_opener_symbol();
  }
}

module bottle_opener_symbol() {
  module outer_shape() {
    copy_x() {
      translate([3,2.5])circle(d=4,$fn=48);
      intersection() {
        translate([0,-6])circle(d=22,$fn=60);
        square([4,20]);
      }
      intersection() {
        translate([0,2.5])circle(r=5,$fn=48);
        translate([0,-5])square([10,7.5]);
      }
      difference() {
        translate([0,-5])square([5,3.5]);
        translate([4.5,-4])circle(r=3,$fn=48);
      }
    }
  }
  module inner_shape() {
    difference() {
      hull()copy_x() {
        translate([2.5,2.3])circle(d=2,$fn=24);
        intersection() {
          translate([0,2.5])circle(r=3.5,$fn=48);
          translate([0,-5])square([10,7.5]);
        }
      }
      difference() {
        translate([0,-2])circle(d=5,$fn=24);
        translate([0,5])circle(d=10.5,$fn=48);
      }
    }
  }
  difference() {
    outer_shape();
    inner_shape();
  }
}

module back_hook_cutout() {
  cube2([50,0.5*2,50],TTT);
  translate([0,0,-3]) {
    cube2([50,3,17],TFT);
    translate([0,3])hull() {
      cube2([50,1.1,20],TTT);
      cube2([50,3.1,18],TTT);
      translate([0,-2])cube2([50,3.1,14],TTT);
    }
    translate([0,4,8])hull() {
      cube2([50,1.1,4],TTT);
      cube2([50,3.1,2],TTT);
    }
    
    hull() {
      translate([0,3,-9]) cube2([50,4,0.2],TFF);
      translate([0,3,-10]) cube2([50,1,1.2],TFF);
    }
    hull() {
      translate([0,0,-10.5+3]) cube2([50,3,0.01],TFF);
      translate([0,0,-10.5]) cube2([50,0.01,5],TFF);
    }
    translate([0,0,-9.3]) cube2([50,3,5],TFF);
  }
}

default_main_font = [
  8, // size
  "Bahnschrift:style=Light SemiCondensed", // font
  "center", // halign
  "center", // valign
];
default_top_font = [
  4, // size
  "Arial:style=Bold", // font
  "center", // halign
  "center", // valign
];

module wera_holder(
    handle_d=36,
    handle_hex_d=26.7,
    handle_bottom_circle_dia=23,
    shaft_d=7,
    top_shaft_d=11.5,
    symbol_type="flat",
    text="5.5",
    handle_sides=6,
    main_font=default_main_font,
    top_font=default_top_font) {
  body_width=handle_d+4;
  handle_hex_wide_d=handle_hex_d+min(handle_hex_d*.09,2)+0.5;
  handle_hole_d=handle_hex_wide_d+0.5;
  shaft_hole_d=shaft_d+1;
  top_shaft_hole_d=top_shaft_d+0.5;
      
  module wera_932_handle() {
    hull () {
      intersection() {
        cylinder(d1=handle_bottom_circle_dia,d2=handle_bottom_circle_dia+13,h=4,$fn=48);
        cylinder(d=handle_hex_wide_d,h=51,$fn=48,center=true);
        cylinder(d=(handle_hex_d+0.3)*2/sqrt(3),h=50,$fn=handle_sides,center=true);
      }
      translate([0,0,6])cylinder(d=handle_hole_d,h=11,$fn=48);
      translate([0,2,6])cylinder(d=handle_hole_d,h=11,$fn=48);
    }
    translate([0,0,-3])cylinder(d1=top_shaft_hole_d,d2=top_shaft_hole_d+4,h=3.01,$fn=48);
    translate([0,0,-11])cylinder(d1=top_shaft_hole_d,d2=top_shaft_hole_d,h=11.01,$fn=48);
    translate([0,0,-30])cylinder(d=shaft_hole_d,h=20.01,$fn=48);
  }
  module body_hull() {
    hull() {
      cube2([body_width-2,44,20],TFT);
      cube2([body_width-2,45.01,18],TFT);
      cube2([body_width,44,18],TFT);
      translate([0,0,-5]) {
        cube2([body_width-2,9,20],TFT);
        cube2([body_width,9,18],TFT);
      }
    }
  }
  difference() {
    body_hull();
    
    back_hook_cutout();
    translate([0,25,4])wera_932_handle();
    
    hull()for(a=[0,1])translate([0,25+a*20])cylinder(d=shaft_hole_d,h=50,center=true,$fn=24);
    hull()for(a=[0,1])translate([0,25+a*20,-(1-a)*7])cylinder(d=top_shaft_hole_d,h=50,$fn=24);
    translate([0,108-body_width])scale([0.5,1])rotate([0,0,45])cube2([50,50,50],TTT);
  }

  text_center_x=body_width/2-7.4;
  text = concat([], text); // convert to list
  translate([text_center_x,45])rotate([90,0,180]) {
    if (len(text) > 1) {
      translate([0,5])linear_extrude(height = 1) {
          text(text[0], size = top_font[0], font = top_font[1], halign = top_font[2], valign = top_font[3]);
        }
      translate([0,-3])linear_extrude(height = 1) {
          text(text[1], size = main_font[0], font = main_font[1], halign = main_font[2], valign = main_font[3]);
        }
    } else {
      linear_extrude(height = 1) {
          text(text[0], size = main_font[0], font = main_font[1], halign = main_font[2], valign = main_font[3]);
        }
    }
    }
  translate([-text_center_x,45])rotate([90,0,180])linear_extrude(height = 1) {
    symbol(symbol_type);
  }
}

module wera_bottle_opener_holder() {
  difference() {
    wera_holder(40,23,21.5,14,14,"bottle_opener","");
    translate([0,25,-15]) hull(){
      cylinder(d1=24,d2=2,h=11);
      translate([0,20,3])cylinder(d1=24,d2=2,h=11);
    }
    translate([0,53,-12])cylinder(d1=42,d2=2,h=20,$fn=4);
  }
}

module spacer(width=5) {
  chamfer=min(2,max(0,width-2));
  difference() {
    union() {
      hull() {
        cube2([width-chamfer,9,20],TFT);
        cube2([width-chamfer,10,18],TFT);
        cube2([width,9,20-chamfer],TFT);
        cube2([width,10-chamfer/2,18],TFT);
        translate([0,0,-5]) {
          cube2([width-chamfer,9,20],TFT);
          cube2([width-chamfer,10,18],TFT);
          cube2([width,9,20-chamfer],TFT);
          cube2([width,10-chamfer/2,18],TFT);
        }
      }
    }
    back_hook_cutout();
  }
}

module rail(width=90,holes_distance=45) {
  pegs=floor(width/holes_distance);
  difference() {
    union() {
      cube2([width,15,4.5],TTF);
      translate([0,0,1.5])hull() {
        cube2([width,20,1],TTT);
        cube2([width,18,3],TTT);
      }
    }
    start=(holes_distance*(pegs-1))/2;
    for(a=[0:pegs-1])translate([a*holes_distance-start,0,-.01]) {
      cylinder(d=8,h=0.71,$fn=24);
      translate([0,0,0.7])cylinder(d1=8,d2=2,h=3,$fn=24);
      cylinder(d=4,h=10,$fn=24);
    }
  }
}

module rail_with_peg_holes(width=90,holes_distance=45) {
  pegs=floor(width/holes_distance);
  difference() {
    union() {
      cube2([width,15,4.5],TTF);
      translate([0,0,1.5])hull() {
        cube2([width,20,1],TTT);
        cube2([width,18,3],TTT);
      }
    }
    start=(holes_distance*(pegs-1))/2;
    for(a=[0:pegs-1])translate([a*holes_distance-start,0,-.01]) {
      cylinder(d=8,h=0.71,$fn=24);
      translate([0,0,0.7])cylinder(d1=8,d2=2,h=3,$fn=24);
      cylinder(d=4,h=10,$fn=24);
      
      // peg adapter hole
      hull()copy_y()translate([0,3.1,3.01])cylinder(d=4.85,h=5,$fn=24);
    }
  }
}

module rail_peg_m4() {
  difference() {
    union() {
      hull() {
        cylinder(d=9,h=1,$fn=48);
        translate([0,0,1])cylinder(d=11,h=4.01,$fn=48);
      }
      hull()copy_y()translate([0,3.1,5.01]){
        cylinder(d=4.8,h=2-0.2,$fn=24);
        cylinder(d=4.8-0.4,h=2,$fn=24);
      }
    }
    translate([0,0,-.01])cylinder(d=7*2/sqrt(3),h=4,$fn=6);
    translate([0,0,4.2])cylinder(d=4.1,h=10,$fn=24);
  }
}
module rail_peg_screw_4mm() {
  h1=5;
  h2=2;
  difference() {
    union() {
      hull() {
        cylinder(d=9,h=1.01,$fn=48);
        translate([0,0,1])cylinder(d=11,h=h1-1,$fn=48);
      }
      hull()copy_y()translate([0,3.1,h1]){
        cylinder(d=4.8,h=h2-0.2,$fn=24);
        cylinder(d=4.8-0.4,h=h2,$fn=24);
      }
    }
    translate([0,0,-.01])cylinder(d=2.7,h=10,$fn=24);
    translate([0,0,h1+h2-1.9])cylinder(d1=1,d2=4,h=2,$fn=24);
  }
}

module rail_ikea_skadis(pegs=2) {
  spacing=40;
  width=pegs*spacing;
  hook_length=12;
  hook_width=4.5;
  board_thickness=5.2;
  rail_back_height=15;
  union() {
    cube2([width,rail_back_height,4.5],TTF);
    translate([0,0,1.5])hull() {
      cube2([width,20,1],TTT);
      cube2([width,18,3],TTT);
    }
    
    start=(spacing*(pegs-1))/2;
    for(a=[0:pegs-1])translate([a*spacing-start,-rail_back_height/2]) {
      translate([0,0,4.5+board_thickness])cube_chamfered([hook_width,hook_length,hook_width],TFF,0.7);
      translate([0,0,4.5-1])cube_chamfered([hook_width,hook_width,1+board_thickness+hook_width],TFF,0.7);
    }
  }
}


module rail_inch_pegboard(pegs=2,board_thickness=0) {
  spacing=25.4;
  width=pegs*spacing;
  pin_d=6.0;
  rail_back_height=15;
  rail_thickness=4;
  union() {
    cube2([width,rail_back_height,rail_thickness],TTF);
    translate([0,0,1.5])hull() {
      cube2([width,20,1],TTT);
      cube2([width,18,3],TTT);
    }
    
    start=(spacing*(pegs-1))/2;
    for(a=[0:pegs-1])translate([a*spacing-start,-rail_back_height/2+pin_d/2,rail_thickness-.01]) {
      cylinder(d=pin_d,h=board_thickness-0.5,$fn=24);
      translate([0,0,board_thickness-0.5])for(b=[0:4:50])hull()for(c=[0,4])translate([0,-7])rotate([b+c,0])translate([0,7])cylinder(d=pin_d,h=1,$fn=24);
    }
  }
}
