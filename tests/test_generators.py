"""测试生成器"""

import unittest
from src.templates.suo_han_template import SuoHanTemplate
from src.templates.wei_tuo_xie_yi_template import WeiTuoXieYiTemplate
from src.templates.shou_quan_wei_tuo_shu_template import ShouQuanWeiTuoShuTemplate
from src.templates.fa_lv_fen_xi_template import FaLvFenXiTemplate


class TestTemplates(unittest.TestCase):
    """模板测试"""

    def test_suo_han_template(self):
        """测试所函模板"""
        template = SuoHanTemplate()
        data = {
            "law_firm_name": "测试律师事务所",
            "lawyer_name": "李律师",
            "license_number": "110123456789",
            "client_name": "张三",
            "client_address": "北京市朝阳区",
            "letter_date": "2024-01-01",
            "content": "测试内容"
        }
        
        result = template.generate(data)
        self.assertIn("测试律师事务所", result)
        self.assertIn("李律师", result)

    def test_wei_tuo_xie_yi_template(self):
        """测试委托协议模板"""
        template = WeiTuoXieYiTemplate()
        data = {
            "client_name": "张三",
            "client_id": "110123456789012345",
            "law_firm_name": "测试律师事务所",
            "lawyer_name": "李律师",
            "license_number": "110123456789",
            "legal_matter": "合同纠纷",
            "service_scope": "代理诉讼",
            "fees": "5000元",
            "payment_method": "银行转账",
            "agreement_date": "2024-01-01"
        }
        
        result = template.generate(data)
        self.assertIn("委托协议", result)
        self.assertIn("张三", result)

    def test_shou_quan_wei_tuo_shu_template(self):
        """测试授权委托书模板"""
        template = ShouQuanWeiTuoShuTemplate()
        data = {
            "client_name": "张三",
            "client_id": "110123456789012345",
            "client_address": "北京市朝阳区",
            "agent_name": "李四",
            "agent_id": "110123456789012346",
            "agent_job": "律师",
            "agency_matter": "诉讼代理",
            "agency_scope": "全权代理",
            "agency_date": "2024-01-01",
            "valid_period": "一年"
        }
        
        result = template.generate(data)
        self.assertIn("授权委托书", result)
        self.assertIn("张三", result)

    def test_fa_lv_fen_xi_template(self):
        """测试法律分析模板"""
        template = FaLvFenXiTemplate()
        data = {
            "case_name": "合同纠纷案",
            "parties": "原告：张三，被告：李四",
            "background": "背景信息",
            "legal_issues": "法律问题",
            "applicable_laws": "《民法典》",
            "analysis": "法律分析",
            "conclusion": "结论",
            "analyst_name": "王律师",
            "analysis_date": "2024-01-01"
        }
        
        result = template.generate(data)
        self.assertIn("法律分析", result)
        self.assertIn("合同纠纷案", result)


if __name__ == '__main__':
    unittest.main()
