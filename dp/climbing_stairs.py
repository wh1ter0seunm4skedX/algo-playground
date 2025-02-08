import logging
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def climbing_stairs_recursive(n: int) -> int:
    """
    Solve climbing stairs problem recursively (inefficient solution)
    Time complexity: O(2^n)
    Space complexity: O(n) - recursion stack
    """
    def climb(n: int, step: int, path: str) -> int:
        # Base cases
        if n == step:
            logger.info(f"Found valid path: {path} ✓")
            return 1
        if step > n:
            logger.info(f"Invalid path: {path} ✗")
            return 0
        
        # Recursive cases
        logger.info(f"Currently at step {step}, trying paths from: {path}")
        
        # Try taking 1 step
        one_step = climb(n, step + 1, path + "1")
        # Try taking 2 steps
        two_steps = climb(n, step + 2, path + "2")
        
        return one_step + two_steps
    
    logger.info("\n=== Starting Recursive Solution ===")
    result = climb(n, 0, "")
    logger.info(f"Total number of ways: {result}")
    return result

def climbing_stairs_dp(n: int) -> int:
    """
    Solve climbing stairs problem using dynamic programming
    Time complexity: O(n)
    Space complexity: O(n)
    """
    logger.info("\n=== Starting DP Solution ===")
    
    # Initialize dp array
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to climb 0 stairs
    dp[1] = 1  # Base case: one way to climb 1 stair
    
    # Fill dp array
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        logger.info(f"Ways to reach step {i}: {dp[i]} (from step {i-1}: {dp[i-1]} + from step {i-2}: {dp[i-2]})")
    
    logger.info(f"DP array: {dp}")
    logger.info(f"Total number of ways: {dp[n]}")
    return dp[n]

if __name__ == "__main__":
    # Test with a small number of stairs
    n = 10
    logger.info(f"\nSolving climbing stairs problem for n = {n}")
    logger.info("=" * 50)
    
    # Solve using recursive approach
    recursive_result = climbing_stairs_recursive(n)
    
    # Solve using DP approach
    dp_result = climbing_stairs_dp(n)
    
    assert recursive_result == dp_result, "Both solutions should yield the same result"
