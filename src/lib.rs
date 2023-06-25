use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn sum_to_n(n: i64) -> PyResult<i64> {
    // sum of 1 to n with loop
    let mut sum = 0;
    for i in 1..n + 1 {
        sum += i;
    }
    Ok(sum)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_module(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(sum_to_n, m)?)?;
    Ok(())
}
