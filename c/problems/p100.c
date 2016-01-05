#include <stdio.h>
#include <inttypes.h>
#include <stdint.h>
#include <time.h>
#include <math.h>

uint64_t calcNextArrange(uint64_t start);

/**
 * Thoughts: I completely cheesed this problem. I initially realised that
 * the ratio between the blue disks and the total number of disks would tend
 * to the square root of 2. So, I just brute forced it, incrementing the total
 * disks and dividing by the square root of 2. I did make it slightly efficient
 * such as precomputing sqrt(2) and then multiplying by 1/sqrt(2) (also
 * precomputed) and reducing the needed divisions/multiplications. Since the
 * problem was quite old, it was more reasonable to brute force it with the
 * current computing power. It still took around 378.75 seconds to run though.
 *
 * I also realised immediately that the problem was probably intended to be
 * solved using Pell's equation. But, it's been so long since I dealt with that
 * (and I don't even have the code for it anymore), that I decided to just
 * brute force it (in a fast language instead of the usual python). Looking at
 * the problem solution thread, it seems that Pell's equation was indeed the
 * way to solve it. Still, it was nice to get some C practice.
 */
int main(int argc, char **argv) {
  printf("Solving p100...\n");
  clock_t start = clock();

  uint64_t result = calcNextArrange(1e12);

  clock_t end = clock();

  printf("Result: %" PRIu64 "\n", result);
  printf("Elapsed: %f seconds\n", (double)(end-start) / CLOCKS_PER_SEC);

  return 0;
}

/**
 * Given a starting total number, calculates the next number of blue disks
 * which satisfies the given property (as according to problem 100).
 */
uint64_t calcNextArrange(uint64_t start) {
  uint64_t current = start;
  // Precompute 1/sqrt(2).
  double root2i = 1.0/sqrt(2.0);
  double possible;
  uint64_t lower;

  while (1) {
    
    // Values will be around the sum of disks divided by the square root of two
    possible = current * root2i;
    lower = (uint64_t)possible;
    
    // The lower value is the truncated value of the divided value while the
    // upper part is lower+1. We want it to be half the total * (total - 1).
    if ((lower * (lower+1) << 1) == (current * (current-1))) {
      printf("Lower, Current: %" PRIu64 " %" PRIu64 "\n", (lower+1), current);
      return (lower+1);
    }

    current++;
  }
}
