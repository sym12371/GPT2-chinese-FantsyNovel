#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re

def simple_convert_and_clean():
    """简化版本的转换脚本"""
    
    # 获取所有.txt文件
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not txt_files:
        print("当前目录下没有找到.txt文件")
        return
    
    results = []
    
    for filename in txt_files:
        try:
            # 尝试用常见编码读取文件
            content = None
            for encoding in ['utf-8', 'gbk', 'gb2312']:
                try:
                    with open(filename, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                print(f"无法读取文件: {filename}")
                continue
            
            # 清理文本（移除控制字符）
            cleaned = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', content)
            cleaned = cleaned.strip()
            
            # 以UTF-8编码写回文件
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            
            results.append(cleaned)
            print(f"成功处理: {filename}")
            
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {e}")
    
    # 保存到JSON文件
    if results:
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n完成！共处理 {len(results)} 个文件，结果已保存到 output.json")

if __name__ == "__main__":
    simple_convert_and_clean()