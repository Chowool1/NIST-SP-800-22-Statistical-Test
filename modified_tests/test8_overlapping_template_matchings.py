import sp80022suite
from unittest import TestCase
import random

class CustomOverlappingTemplateMatchingTestCase(TestCase):

    def run_overlapping_template_test(self, bit_sequence, template_length=9):
        """
        Overlapping Template Matching Test 실행 및 자동 검증.
        - 비트 시퀀스를 입력으로 받아 NIST Overlapping Template Matching 테스트 통과 여부를 검증하고 결과 출력.
        """
        # 비트 문자열을 바이트 배열로 변환
        byte_sequence = bytes([int(bit) for bit in bit_sequence])

        # Overlapping Template Matching Test 실행
        result = sp80022suite.overlapping_template_matchings(template_length, byte_sequence)
        print(f"Overlapping Template Matching Test Result (template length={template_length}): {result}")

        # 자동 검증: P-값이 0.01 이상이어야 통과
        self.assertGreaterEqual(result, 0.01, "❌ NIST Overlapping Template Matching 테스트 실패: 랜덤성이 부족합니다.")
        
        return result

    def test_sample_file(self):
        """
        sample_bits.txt 파일에서 비트 시퀀스를 읽어와 Overlapping Template Matching 테스트를 수행합니다.
        """
        try:
            with open("sample_bits.txt", "r") as f:
                bit_sequence = f.read().strip()

            # 비어있는 입력에 대한 예외 처리
            if not bit_sequence:
                raise ValueError("⚠️ 입력 파일이 비어 있습니다. 유효한 비트 시퀀스를 제공하세요.")
            
            # 테스트 실행 (기본 template length = 9)
            self.run_overlapping_template_test(bit_sequence, template_length=9)
        except FileNotFoundError:
            print("❌ sample_bits.txt 파일을 찾을 수 없습니다. 파일을 확인하세요.")
        except ValueError as ve:
            print(ve)

    def generate_random_bits(self, num_bits=10000, output_file="sample_bits.txt"):
        """
        랜덤한 비트 시퀀스를 생성하여 파일에 저장합니다.
        - num_bits: 생성할 비트의 개수 (기본값 10000)
        - output_file: 비트를 저장할 파일명 (기본값 sample_bits.txt)
        """
        random_bits = ''.join(str(random.randint(0, 1)) for _ in range(num_bits))
        with open(output_file, "w") as f:
            f.write(random_bits)
        print(f"✅ {num_bits}개의 랜덤 비트 시퀀스가 {output_file}에 저장되었습니다.")

if __name__ == "__main__":
    import unittest
    print("🔍 Starting NIST Overlapping Template Matching Test using sample_bits.txt...")
    # 랜덤 비트 시퀀스 생성 (필요에 따라 호출)
    CustomOverlappingTemplateMatchingTestCase().generate_random_bits(10000)
    unittest.main()

