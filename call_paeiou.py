import os
import paeiou

with open("pa_location.txt") as infile:
        pa_path = os.path.join(infile.readline(), "media/")

def main():
    paeiou.paeiou( 
        mod_id = "com.pa.daedalus.dozer", 
        paeiou_unit_path = "PAEIOU_units/", 
        unit_add_list = "unit_add_list.txt", 
        output_path = "",
        mod_prefix = "dozer",
        server = True,
        client = False,
        pa_path = pa_path
    )

if __name__ == '__main__':
    main()
