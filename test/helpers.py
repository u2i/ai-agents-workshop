import pytest
from functools import wraps
import logging

logger = logging.getLogger(__name__)


def skip_on_error(test_func):
    @wraps(test_func)
    async def wrapper(*args, **kwargs):
        try:
            return await test_func(*args, **kwargs)
        except NotImplementedError:
            pytest.skip("main() function not yet implemented")
        except Exception as e:
            if "connection" in str(e).lower() or "ollama" in str(e).lower():
                pytest.skip(f"Skipping due to model availability: {e}")
            raise

    return wrapper


def probabilistic_test(test_func=None, *, times=3, threshold=1):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            failures = 0
            errors = []
            
            for i in range(times):
                logger.info(f"\033[36mRunning {func.__name__} test {i + 1}/{times}...\033[0m")
                try:
                    await func(*args, **kwargs)
                except Exception as e:
                    failures += 1
                    errors.append(f"Run {i + 1}/{times}: {str(e)}")
            
            if failures > threshold:
                error_msg = f"Test failed {failures}/{times} times (threshold: {threshold}):\n" + "\n".join(errors)
                pytest.fail(error_msg)
        
        return wrapper
    
    if test_func is not None:
        return decorator(test_func)
    
    return decorator
