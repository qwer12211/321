import time
import json
import csv
def getattr(user):
    print("������������  ���," + user)
getattr("������������")
print("������ ����:")

def getatt(ise):
    print("��� ������������� ������ ����������� �������:" + ise)
getatt("Enter")
print("����� ������")
def save_data(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

def load_data():
    try:
        with open('data.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def update_csv(data):
    csv_data = []
    for item in data:
        csv_data.append([item['name'], str(item['age'])])

    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(csv_data)

name = input("������� ��� ���������: ")
name = name.title()
age = float(input("������� ������� ���������: "))

data = load_data()

data.append({'name': name, 'age': age})

save_data(data)

update_csv(data)
info = "��� ������ ���������: %s, ������� ������ ���������: %d" % (name, age)
print(info)
input()

text = ("����� ����� �� ������� ������� ���������� ����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

input()

text = ("����� �� ���� �������� ��������� ��������� ��� �����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("�� ������� ���� ������� ��������� �� ��������� � ������ ������.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("��  ����� ���������� � ���������� �������� ���� ���.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("�����������, �� �������� ���� � ������������ � ������ �������.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

itemsnarukzake = {"������."}
itemsnarukzake.add ("������ ����,")
print("������ ����� �� ����� �������:")
print(*itemsnarukzake)

text = ("������ ������ ��������� ������, � ������ ����� �� ������� �� ���� ���������� ������ ������ ����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

input()

text = ("����� ���� ������� ������ ��������, ���� ��� �� ��������.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("�� ������� ���������� � ���� ������� ����� �� ������ ����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("����� ��������� ����� ���������� ���� �����, � � ������ ������� ���������� ���������, ����� ����.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("�� ������� ����������, ��� ������ �������� � ������ � ������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

print("������ ����� � ����� �������:")
rukzak = {"����� �����", "�����", "���������."}
for i in rukzak:
    print(i)

text = ("�� ����� � ���� ������ �������.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("�� ������ ����� ���� ���������� �����, ��������� ����� � ����������� ���������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

input()

messege = ("����� � ������� ���������: \"��� ���� ��������� ���� ����� �������� ������ ��������?\n")
for char in messege:
     print(char, end='', flush=True)
     time.sleep(0.04)

textA = (" ��� �����?!\n")
print(textA.upper())

fraza = f"{name}, �� ���� �������?"
print(fraza)

def gettra(saewr):
    print( saewr + "��� ��?")
gettra("��: ")


text = ("��� ������� ��� �������� ���������. ����, �����, �� ���������� ����� ����, ��� � ����.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

def getat(ie):
    print("��� ���:" + ie)
getat("������ �������?!")

input()

text = ("��� ������� ��� ���.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)
input()

text = ("�� ������ ����� �� ����. ������, � ������� �� ������, ��� �� �����, ��� � �� ������������, ��������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("�� - ����� ������������ ����� �������������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("�� ���������, ��� ����� ��������� ������, ���� �� ��������� ������ �������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

messege = ("������: \" ���� �� �� �������?.\n")
for char in messege:
     print(char, end='', flush=True)
     time.sleep(0.04)

def gettr(sewr):
    print( sewr + "�������� ����� ���� �� ������������� � ������������.")
gettr("��: ")

input()

messege = ("������: \" ��-��-��!\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("����� ��������� ����\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

input()

messege = ("������:�� ���� ���������, ��� ���� ��� ������ �� ���� �� ����?\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

def getatr(ser):
    print( ser + "��� ���� ��  ���� �����?")
getatr("��: ")

input()

messege = ("������: � ����� �����. �� ��� ��� ����� �� ����� �� ����� � �� ������ ����, �� �� ������� ���� ������� � ������. �, �������, ����� ������������ �� ������ ��������, ���������� ����, � ������ �����!\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

def getar(se):
    print( se + "�� ����������. � ����� �� ����� ���� ������. �� ������ ��� ������� �����")
getar("��: ")

input()

messege = ("������:  ��� ���� ����� ������ ������ �� ������...\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("�� ������ ������� ��������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

messege = ("������:  ������, ����� ���: � ��������� ���� ������. �������� ��� - � � ����� ����, ��� ����� ������� ������� ���� ���������.\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

def getaptr(segr):
    print( segr + "� ���� � ��������?")
getaptr("��: ")

input()

messege = ("������:  � ����� ���� � ���. � ���� ����� ��������� ������� � ������� ��� ������.\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("� ��� �� ���������� ������ ����� ��� �����������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

input()

text = ("����� �������� �������� ��������.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("�� �� ������ �� �������� ���� �����, �������� ��� ������ ��������� �����.\n")
for char in text:
     print(char, end='', flush=True)
     time.sleep(0.04)

text = ("����� �� ������ ������ ��������� ����� � ����� �������� �����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("�� ������ ����������� ���������� ��������� ������ �� ������ �����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = ("��� ��  �� �������� ��� ����������, �� - ��, ��� ��� �������� �������.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

messege = ("������:  ��� ��� �� �������������� ��������?\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

messege = ("������:  �����, ������� ���� ������ �����.\n")
for char in messege:
    print(char, end='', flush=True)
    time.sleep(0.04)

input()

text = (" �� ���������� ����, ���������� �� ���� �������.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

text = (" � ���� �� ������ ������ ����� ����������� � �������� ������� �� ������ ������ ����� �����.\n")
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.04)

print("����� ������ �����")

