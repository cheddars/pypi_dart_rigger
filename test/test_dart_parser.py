import unittest

from dartrig.parser_dsaf import extract_nodes, extract_node


class DartParserTest(unittest.TestCase):
    def test_parse_node(self):
        test_str = (
            "				var node2 = {};\n"
            "				node2['text'] = \"2. 임원의 보수 등\";\n"
            "				node2['id'] = \"39\"; 	\n"
            "				node2['rcpNo'] = \"20220214000604\";\n"
            "				node2['dcmNo'] = \"8384685\";\n"
            "				node2['eleId'] = \"39\";\n"
            "				node2['offset'] = \"1153950\";\n"
            "				node2['length'] = \"10278\";\n"
            "				node2['dtd'] = \"dart3.xsd\";\n"
            "				node2['tocNo'] =  \"37\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
            "				\n"
            "				cnt++;\n"
        )
        r = extract_node(test_str)
        print(r)

    def test_parse_nodes(self):
        test_str = ("				var node2 = {};\n"
                    "				node2['text'] = \"2. 임원의 보수 등\";\n"
                    "				node2['id'] = \"39\"; 	\n"
                    "				node2['rcpNo'] = \"20220214000604\";\n"
                    "				node2['dcmNo'] = \"8384685\";\n"
                    "				node2['eleId'] = \"39\";\n"
                    "				node2['offset'] = \"1153950\";\n"
                    "				node2['length'] = \"10278\";\n"
                    "				node2['dtd'] = \"dart3.xsd\";\n"
                    "				node2['tocNo'] =  \"37\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
                    "				\n"
                    "				cnt++;\n"
                    "				\n"
                    "				\n"
                    "				\n"
                    "				\n"
                    "				\n"
                    "				node1['children'].push(node2);\n"
                    "				\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			treeData.push(node1);\n"
                    "		\n"
                    "			var node1 = {};\n"
                    "			node1['text'] = \"IX. 계열회사 등에 관한 사항\";\n"
                    "			node1['id'] = \"40\";\n"
                    "			node1['rcpNo'] = \"20220214000604\";\n"
                    "			node1['dcmNo'] = \"8384685\";\n"
                    "			node1['eleId'] = \"40\";\n"
                    "			node1['offset'] = \"1164246\";\n"
                    "			node1['length'] = \"8890\";\n"
                    "			node1['dtd'] = \"dart3.xsd\";\n"
                    "			node1['tocNo'] =  \"38\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
                    "			\n"
                    "			cnt++;\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			treeData.push(node1);\n"
                    "		\n"
                    "			var node1 = {};\n"
                    "			node1['text'] = \"X. 대주주 등과의 거래내용\";\n"
                    "			node1['id'] = \"41\";\n"
                    "			node1['rcpNo'] = \"20220214000604\";\n"
                    "			node1['dcmNo'] = \"8384685\";\n"
                    "			node1['eleId'] = \"41\";\n"
                    "			node1['offset'] = \"1173140\";\n"
                    "			node1['length'] = \"23049\";\n"
                    "			node1['dtd'] = \"dart3.xsd\";\n"
                    "			node1['tocNo'] =  \"39\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
                    "			\n"
                    "			cnt++;\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "			treeData.push(node1);\n"
                    "		\n"
                    "			var node1 = {};\n"
                    "			node1['text'] = \"XI. 그 밖에 투자자 보호를 위하여 필요한 사항\";\n"
                    "			node1['id'] = \"42\";\n"
                    "			node1['rcpNo'] = \"20220214000604\";\n"
                    "			node1['dcmNo'] = \"8384685\";\n"
                    "			node1['eleId'] = \"42\";\n"
                    "			node1['offset'] = \"1196193\";\n"
                    "			node1['length'] = \"4368\";\n"
                    "			node1['dtd'] = \"dart3.xsd\";\n"
                    "			node1['tocNo'] =  \"40\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
                    "			\n"
                    "			cnt++;\n"
                    "			\n"
                    "			\n"
                    "				node1['children'] = [];\n"
                    "			\n"
                    "			\n"
                    "			\n"
                    "				var node2 = {};\n"
                    "				node2['text'] = \"1. 공시내용 진행 및 변경사항\";\n"
                    "				node2['id'] = \"43\"; 	\n"
                    "				node2['rcpNo'] = \"20220214000604\";\n"
                    "				node2['dcmNo'] = \"8384685\";\n"
                    "				node2['eleId'] = \"43\";\n"
                    "				node2['offset'] = \"1196325\";\n"
                    "				node2['length'] = \"141\";\n"
                    "				node2['dtd'] = \"dart3.xsd\";\n"
                    "				node2['tocNo'] =  \"41\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
                    "				\n"
                    "				cnt++;\n"
                    "				\n"
                    "				\n"
                    "				\n"
                    "				\n"
                    "				\n"
                    "				node1['children'].push(node2);\n"
                    "				\n"
                    "			\n"
                    "				var node2 = {};\n"
                    "				node2['text'] = \"2. 우발부채 등에 관한 사항\";\n"
                    "				node2['id'] = \"44\"; 	\n"
                    "				node2['rcpNo'] = \"20220214000604\";\n"
                    "				node2['dcmNo'] = \"8384685\";\n"
                    "				node2['eleId'] = \"44\";\n"
                    "				node2['offset'] = \"1196470\";\n"
                    "				node2['length'] = \"2828\";\n"
                    "				node2['dtd'] = \"dart3.xsd\";\n"
                    "				node2['tocNo'] =  \"42\";  //eleId 가 toc 순번하고 동일 하지 않은 문서가 존재함.\n"
                    "				\n"
                    "				cnt++;\n"
                    "				")

        r = extract_nodes(test_str)
        for i in r:
            print(i)