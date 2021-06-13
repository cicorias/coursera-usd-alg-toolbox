#include <iostream>
#include <vector>
// #include <algorithm>

typedef long long int int64;

int64 MaxPairwiseProduct(const std::vector<int64_t>& numbers) {
    int64_t max_product = 0;
    int64_t n = numbers.size();

    for (int64_t first = 0; first < n; ++first) {
        for (int64_t second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

int main() {
    int64_t n;
    std::cin >> n;
    std::vector<int64_t> numbers(n);
    for (int64_t i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << "using 64" << sizeof(int64_t) << "\n";
    std::cout << MaxPairwiseProduct(numbers) << "\n";
    return 0;
}
