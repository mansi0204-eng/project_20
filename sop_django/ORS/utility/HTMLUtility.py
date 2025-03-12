

class HTMLUtility:

    @staticmethod
    def get_list_from_dict(name, selected_val, data_dict):
        print("preload-5")
        sb = [
            f"<select style=\"width:101%; text-align-last:center;\" class='form-control' name='{name}'>"
        ]
        sb.append("\n<option selected value=''>-----------Select-----------</option>")
        print("preload-6")
        for key, val in data_dict.items():
            if key == selected_val:
                sb.append(f"\n<option selected value='{key}'>{val}</option>")
            else:
                sb.append(f"\n<option value='{key}'>{val}</option>")
        print("preload-7")
        sb.append("\n</select>")
        return "".join(sb)

    @staticmethod
    def get_list_from_objects(name, selected_val, data_list):
        print("preload-8")
        sb = [
            f"<select style=\"width:101%; text-align-last:center;\" class='form-control' name='{name}'>"
        ]
        sb.append("\n<option selected value=''>-----------Select-----------</option>")
        print("preload-9")
        for obj in data_list:
            print("preload-10")
            key = obj.get_key()
            val = obj.get_value()
            print("preload-11")
            if key == str(selected_val):
                sb.append(f"\n<option selected value='{key}'>{val}</option>")
            else:
                sb.append(f"\n<option value='{key}'>{val}</option>")
            print("preload-12")
        sb.append("\n</select>")
        return "".join(sb)
