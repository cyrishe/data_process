from itertools import product
import random
import textwrap


def generate_truth_table(inputs):
    return [(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)) for _ in range(2**inputs)]

def generate_logic_expression(truth_table):
    num_inputs = len(truth_table[0]) - 1
    
    expressions = []

    for row in truth_table:
        input_values = row[0:-1]
        output_value = row[-1]

        terms = []
        for i in range(num_inputs-1):
            if input_values[i] == 0:
                terms.append(f"~X{i + 1}")
            else:
                terms.append(f"X{i + 1}")

        expression = " & ".join(terms) if output_value == 1 else " | ".join(terms)
        expressions.append(f"({expression})")

    final_expression = " | ".join(expressions)
    return final_expression

# Example usage:
num_inputs = 3
truth_table = generate_truth_table(num_inputs+1)
print(truth_table)
logic_expression = generate_logic_expression(truth_table)
print(logic_expression)
import random

def generate_truth_table(input_nums):
    # 根据位数生成二次数组
    # result = []
    # if input_nums == 2:
    #     result = [[0,0],[0,1],[1,0],[1,1]]
    # elif input_nums == 3:
    #     result = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    # elif input_nums == 4:
    #     result = [[0,0,0,0],[0,]]
    if input_nums !=2:
        input_nums=input_nums-1
        result = []
        for item in generate_truth_table(input_nums):
            item1 = [ i for i in item]
            item1.append(0)
            result.append(item1)
            item2 = [ i for i in item]
            item2.append(1)
            result.append(item2)
        print("result:",result)
        return result
    else:
        return [[0,0],[0,1],[1,0],[1,1]]

# print(generate_truth_table(4))

def generate_random_y(truth_table_list):
    for i in truth_table_list:
        i.append(random.randint(0,1))
    return truth_table_list

a = generate_random_y(generate_truth_table(4))
for i in a:
    print(a.index(i),i)

"""根据真值表生成表达式"""
# def generate_expression(truth_table_list):
#     for item_list in truth_table_list:
#         if item_list.top()==1:
            
def generate_logic_expression(truth_table):
    num_inputs = len(truth_table[0]) - 1  # Subtract 1 for the output column
    
    expressions = []

    for row in truth_table:
        input_values = row[:-1]
        output_value = row[-1]
        # print(input_values)
        # print(output_value)
        terms = []
        num = num_inputs-1
        for i in range(num_inputs):
            if input_values[i] == 0:
                terms.append(f"~x{i + 1 + num}")
                num-=2
            else:
                terms.append(f"x{i + 1 + num}")
                num-=2

        # expression = " & ".join(terms) if output_value == 1 else " | ".join(terms)
        # expressions.append(f"({expression})")

        if output_value == 1:
            expression = " && ".join(terms)
            expressions.append(f"({expression})")
    final_expression = " || ".join(expressions)
    return final_expression

b = generate_logic_expression(a)
print(b)


'''num_input = 2,3,4,5'''

"""生成verilog文件"""
def generate_verilog_file(output_file_path, num_inputs):
    # 随机生成一个三位输入的真值表
    truth_table = generate_random_y(generate_truth_table(num_inputs))
    truth_table_in_verilog = (
    "//Inputs | Outputs\n"
    )
    str1 = ""
    for item in truth_table:
        str1+="//"
        for i in range(len(item)-1):
            str1 = str1 + str(item[i]) +" "
        str1 += "| " + str(item[num_inputs])
        str1 +="\n"

    truth_table_in_verilog += f"""\
{str1}
    """
    if num_inputs==3:
    # 创建 Verilog 文件内容
        verilog_code = textwrap.dedent(f"""\
module truthtable(input x3, input x2, input x1, output f );
    """)
    elif num_inputs==2:
        verilog_code = textwrap.dedent(f"""\
module truthtable(input x2, input x1, output f );
    """)
    elif num_inputs==4:
        verilog_code = textwrap.dedent(f"""\
module truthtable(input x4, input x3, input x2, input x1, output f );
    """)
    else:
        verilog_code = textwrap.dedent(f"""\
module truthtable(input x5, input x4, input x3, input x2, input x1, output f );
    """)
    expression_in_verilog = textwrap.dedent(f"""\
        assign f = {generate_logic_expression(truth_table)};
    endmodule
    """)
    # 将 Verilog 代码写入文件
    with open(output_file_path, 'w') as verilog_file:
        verilog_file.write(truth_table_in_verilog)
        verilog_file.write(verilog_code)
        verilog_file.write(expression_in_verilog)
        
        
# 输出三千个表
for i in range(1000,3000):
# 设置输出文件路径和输入数量
    output_file_path = f'C:/Users/yyjiang/Apps/Coding/Codingfiles/Truthtables/{"truthtable_answer_"+str(i)+".v"}'
    num_inputs_list = [2,3,4,5]
    num_inputs = random.choice(num_inputs_list)
    # 生成 Verilog 文件
    generate_verilog_file(output_file_path, num_inputs)

