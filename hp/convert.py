import json
import re

def convert_item(item):
    """
    递归处理数据结构，将 htmlSrc 或 page 数据项转换为 imageSrc (.png) + audioSrc (.mp3)
    """
    if isinstance(item, dict):
        new_dict = {}
        for key, value in item.items():
            # 转换属性名称及后缀
            if key == "htmlSrc":
                # 将 .html 替换为 .png，并将键名改为 imageSrc
                new_dict["imageSrc"] = re.sub(r'\.html$', '.png', value)
            else:
                new_dict[key] = convert_item(value)
        
        # 补全/确保 audioSrc 与 imageSrc 配对存在
        if "imageSrc" in new_dict and "audioSrc" not in new_dict:
            new_dict["audioSrc"] = re.sub(r'\.png$', '.mp3', new_dict["imageSrc"])
            
        return new_dict

    elif isinstance(item, list):
        return [convert_item(element) for element in item]
    
    return item

def process_file(input_file_path, output_file_path):
    """
    读取、转换并保存 JSON 文件
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 执行转换
        converted_data = convert_item(data)
        
        # 写入新文件
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(converted_data, f, ensure_ascii=False, indent=2)
            
        print(f"✅ 转换完成！已保存至: {output_file_path}")
        
    except Exception as e:
        print(f"❌ 处理文件时出错: {e}")

if __name__ == "__main__":
    # 输入与输出文件名
    input_json = "data.json"
    output_json = "data_converted.json"
    
    process_file(input_json, output_json)
