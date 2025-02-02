import sp80022suite
import random
import os

class NistTestSuite:

    def __init__(self, num_bits=1000000, num_iterations=10):
        self.num_bits = num_bits
        self.num_iterations = num_iterations

    def generate_random_bits(self, iteration):
        """
        Iteration 별로 다른 랜덤 비트 시퀀스를 생성하고 파일에 저장합니다.
        """
        random_bits = ''.join(str(random.randint(0, 1)) for _ in range(self.num_bits))
        file_name = f"sample_bits_{iteration}.txt"
        with open(file_name, "w") as f:
            f.write(random_bits)
        return file_name

    def run_test_multiple_times(self, test_name, test_func, *args):
        p_values = []
        pass_count = 0

        print(f"\nRunning {test_name} ({self.num_iterations} iterations):")
        for iteration in range(1, self.num_iterations + 1):
            try:
                # Iteration별로 새로운 랜덤 비트 시퀀스를 생성
                file_name = self.generate_random_bits(iteration)
                with open(file_name, "r") as f:
                    bit_sequence = f.read().strip()
                byte_sequence = bytes([int(bit) for bit in bit_sequence])

                # 테스트 실행
                p_value = test_func(*args, byte_sequence)

                # 결과 출력 및 Pass/Fail 판정
                result = "Pass" if p_value >= 0.01 else "Fail"
                print(f"{test_name} - Iteration {iteration}: P-value = {p_value:.6f} ({result})")

                p_values.append(p_value)
                if result == "Pass":
                    pass_count += 1

                # 파일 삭제 (필요 시 유지 가능)
                os.remove(file_name)

            except Exception as e:
                print(f"Error running {test_name} in iteration {iteration}: {str(e)}")

        # Pass rate 및 평균 P-value 계산
        avg_p_value = sum(p_values) / len(p_values) if p_values else 0
        pass_rate = (pass_count / self.num_iterations) * 100
        print(f"\n{test_name}: Pass Rate = {pass_rate:.2f}%, Avg P-value = {avg_p_value:.6f}\n")

    def run_all_tests(self):
        # Frequency Test
        self.run_test_multiple_times("Frequency Test", sp80022suite.frequency)

        # Block Frequency Test
        self.run_test_multiple_times("Block Frequency Test", sp80022suite.block_frequency, 128)

        # Runs Test
        self.run_test_multiple_times("Runs Test", sp80022suite.runs)

        # Longest Run of Ones Test
        self.run_test_multiple_times("Longest Run of Ones Test", sp80022suite.longest_run_of_ones)

        # Binary Matrix Rank Test
        self.run_test_multiple_times("Binary Matrix Rank Test", sp80022suite.rank)

        # Discrete Fourier Transform Test
        self.run_test_multiple_times("Discrete Fourier Transform Test", sp80022suite.discrete_fourier_transform)

        # Non-Overlapping Template Matching Test
        self.run_test_multiple_times("Non-Overlapping Template Matching Test", sp80022suite.non_overlapping_template_matchings, 4)

        # Overlapping Template Matching Test
        self.run_test_multiple_times("Overlapping Template Matching Test", sp80022suite.overlapping_template_matchings, 9)

        # Universal Test
        self.run_test_multiple_times("Universal Test", sp80022suite.universal)

        # Linear Complexity Test
        self.run_test_multiple_times("Linear Complexity Test", sp80022suite.linear_complexity, 1000)

        # Serial Test
        self.run_test_multiple_times("Serial Test", sp80022suite.serial, 6)

        # Approximate Entropy Test
        self.run_test_multiple_times("Approximate Entropy Test", sp80022suite.approximate_entropy, 6)

        # Cumulative Sums Test
        self.run_test_multiple_times("Cumulative Sums Test", sp80022suite.cumulative_sums)

        # Random Excursions Test
        self.run_test_multiple_times("Random Excursions Test", sp80022suite.random_excursions)

        # Random Excursions Variant Test
        self.run_test_multiple_times("Random Excursions Variant Test", sp80022suite.random_excursions_variant)


if __name__ == "__main__":
    # 통합 테스트 실행
    nist_test_suite = NistTestSuite(num_bits=1000000, num_iterations=10)
    nist_test_suite.run_all_tests()

