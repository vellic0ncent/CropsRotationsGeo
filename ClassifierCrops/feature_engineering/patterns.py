def provide_culture_and_culture_group_encodings(data):

    def seqToCode(seq):
        code = ''
        usedCodeValues = {}
        codeValue = 'a'
        for el in seq:
            if el in usedCodeValues:
                code += usedCodeValues[el]
            else:
                code += codeValue
                usedCodeValues[el] = codeValue
                codeValue = chr(ord(codeValue) + 1)
        return code

    data['cultuCode'] = data.apply(lambda row: seqToCode([row[column] \
                                                          for column in data.columns \
                                                          if column.startswith('CODE_CULTU_')]), axis=1)
    data['groupCode'] = data.apply(lambda row: seqToCode([row[column] \
                                                          for column in data.columns \
                                                          if column.startswith('CODE_GROUP_')]), axis=1)
    return data