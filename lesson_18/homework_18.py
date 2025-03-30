import logging

logging.basicConfig(
    filename="factorial_logger.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def factorial_gen(n):
    result = 1
    for i in range(n):
        result *= i + 1
        logger.info(f"Calling factorial({i+1}). Result: 1{result}")
        yield result


if __name__ == '__main__':
    gen = factorial_gen(5)
    next(gen)
    next(gen)
    next(gen)
    next(gen)
    next(gen)


