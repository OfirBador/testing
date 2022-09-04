"""
--------------------------------------------------------------------------
Author: Ofir Bador (obador@akamai.com)
version: 1.0.0
--------------------------------------------------------------------------
"""
import json
import os
import csv

index_keys2 = 0
MINIMUN_SP = 5
MAXIMUN_SP = 60


def az_login(subscription):
    """
    Login and sign in to the Azure Cli page and navigate to the inserted subscription
    getsecret() function will activate after a successful connection
    :param subscription:(str) the chosen subscription to revel its key vault secrets
    """
    os.system("az login")
    print("Azure login, please make sure to get permission with Azure Cli page")
    print("Azure permission granted, directing to subscription")
    print("current subscription --> " + subscription)
    os.system("az account set --subscription " + subscription + " 2>/dev/null")
    print("--------------------------------------------------------------------------------")
    getsecret()


def getsecret():
    global index_keys2
    """
    Navigate the current subscription(entered in az_login(subscription) function) in the path below:
    keyvault list -> keyvault secret list -> enabled secret
    Only the activated secret that contains a Service Principal format will be printed on the terminal and  saved to
    a file in local directory named "keyvualt.csv" with the function search_keys(written below)
    :return: (file): "keyvualt.csv"
    """
    i1 = 0
    vault = False
    file_csv = open("keyvualt.csv", "a", newline="")
    table_top = ("vault name", "vault id", "secret3letter")
    new_write = csv.writer(file_csv)
    new_write.writerow(table_top)
    keys = getjson_az("az keyvault list")
    # keys.get('name')
    print("-----------------------------entering keyvault list-----------------------------")
    for i in keys:
        index_keys2 = 0
        print("\n" + color("yellow") + "Current vault name: " + keys[i1]['name'] + color("gray"))
        try:
            keys2 = getjson_az("az keyvault secret list --vault-name " + keys[i1]['name'])
            print(color("green") + "______________Vault name_____________|______________________Vault id___________"
                                   "____________|""_""Secret" + color("gray"))
            vault = True
            search_keys(keys, keys2, i1, new_write)

        except Exception as e:
            if not vault:
                print(color("red") + "--------------No permission to get into the vault-------------" + color("gray"))

        vault = False
        i1 += 1

    file_csv.close()
    os.system("az logout")


def search_keys(keys, keys2, i1, new_write):
    """
    Gets keys and keys2 as Json formats searching in keys2 if it contains enable secret, prints the first 3 letters
     And storing them in csv format.
    :param keys: key vault list in Json format
    :param i1: the current index in keys
    :param keys2: secret list in Json format
    :param new_write: csv writer for the file
    :return: True/False if secret is in activation mode
    """
    global index_keys2
    for j in keys2:
        try:
            secret = getjson_az("az keyvault secret show --id https://" + keys[i1]['name'] +
                                ".vault.azure.net/secrets/" + keys2[index_keys2]['name'])
            v_name = str(keys[i1]['name'])
            v_id = keys2[index_keys2]['name']
            s3num = secret['value'][0:3]
            if MINIMUN_SP < len(secret['value']) < MAXIMUN_SP:
                if secret['value'][5] == '~':
                    print(v_name, space(35, v_name), "|", v_id, space(50, v_id), "|", s3num, space(30, s3num))
                    line = (v_name, v_id, s3num)
                    new_write.writerow(line)
            index_keys2 += 1
        except:
            print(color("red") + keys2[index_keys2]['name'] + "------------------secret is disable" + color("gray"))
            index_keys2 += 1

    index_keys2 += 1


def getjson_az(command):
    """
    Run the selected command in the shell to get Azure data in Json format
    :param command: the chosen String to run from Azure
    :return: Azure data in Json format
    """
    return json.loads(os.popen(command).read())


def space(num, name):
    """
    space objects to get equal gaps
    :param num: number of spaces between the lines
    :param name: the string to space from
    :return: number of space multiply with the object
    """
    return " " * (num - len(name))


def color(shade):
    """
    Changing the font to the desired shade, the color that can be selected - green, yellow, red, gray
    :param shade: the selected color to replace
    :return: the code for the selected color
    """
    if shade == 'green':
        return "\u001b[32;1m"
    elif shade == 'yellow':
        return "\u001b[33;1m"
    elif shade == 'red':
        return "\u001b[31;1m"
    elif shade == 'gray':
        return "\u001b[38;1m"


def main():
    az_login("34e73380-a45c-4136-b7ee-f0b7717d2036")


if __name__ == '__main__':
    main()
