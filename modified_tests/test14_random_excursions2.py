import random
import sp80022suite
from unittest import TestCase

class CustomRandomExcursionsTestCase(TestCase):
    
    def run_random_excursions_test(self, bit_sequence):
        """
        Random Excursions Test 실행 및 자동 검증.
        """
        # 비트 문자열을 바이트 배열로 변환
        byte_sequence = bytes([int(bit) for bit in bit_sequence])
        
        # Random Excursions Test 실행
        try:
            result = sp80022suite.random_excursions(byte_sequence)
            print(f"Random Excursions Test Result: {result}")
            self.assertGreaterEqual(result, 0.01, "❌ NIST Random Excursions Test 실패: 랜덤성이 부족합니다.")
        except ValueError as e:
            print(f"오류 발생: {str(e)}")

    def test_sample_file(self):
        """
        sample_bits.txt 파일에서 비트 시퀀스를 읽어와 Random Excursions Test를 수행합니다.
        """
        try:
            with open("sample_bits.txt", "r") as f:
                bit_sequence = f.read().strip()

            if not bit_sequence:
                raise ValueError("⚠️ 입력 파일이 비어 있습니다.")
            
            # 테스트 실행
            self.run_random_excursions_test(bit_sequence)
        except FileNotFoundError:
            print("❌ sample_bits.txt 파일을 찾을 수 없습니다.")
        except ValueError as ve:
            print(ve)

    def generate_random_bits_with_crossings(self, num_bits=1000000, min_crossings=500):
        """
        랜덤한 비트 시퀀스를 생성하고 0 교차점을 보장합니다.
        """
        while True:
            random_bits = [random.choice((0, 1)) for _ in range(num_bits)]
            crossings = self.count_zero_crossings(random_bits)
            if crossings >= min_crossings:
                with open("sample_bits.txt", "w") as f:
                    f.write(''.join(map(str, random_bits)))
                print(f"✅ {num_bits}개의 비트 시퀀스가 {crossings}개의 교차점을 포함하고 sample_bits.txt에 저장되었습니다.")
                break
            else:
                print(f"교차점 부족: {crossings}개. 재생성 중...")

    def count_zero_crossings(self, bit_sequence):
        """
        0을 기준으로 한 교차점의 개수를 계산합니다.
        """
        S_k = 0
        crossings = 0
        for bit in bit_sequence:
            S_k += 1 if bit == 1 else -1
            if S_k == 0:
                crossings += 1
        return crossings


if __name__ == "__main__":
    import unittest
    print("🔍 Starting NIST Random Excursions Test using sample_bits.txt...")
    CustomRandomExcursionsTestCase().generate_random_bits_with_crossings(1000000)
    unittest.main()

