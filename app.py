import streamlit as st
import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge import mergeSort

# ========== الگوریتم‌های داخلی ==========

def run_merge_sort(arr):
    mergeSort(arr, 0, len(arr) - 1)
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1): heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# ========== توضیحات الگوریتم‌ها ==========

algorithm_details = {
    "Bubble Sort (مرتب‌سازی حبابی)": (
        bubble_sort,
        "🔵 ساده‌ترین الگوریتم: بارها دو عنصر کناری را مقایسه می‌کند و جابجا می‌کند تا لیست مرتب شود. (O(n²)"
    ),
    "Insertion Sort (مرتب‌سازی درج)": (
        insertion_sort,
        "🟢 مانند مرتب‌سازی دستی: هر عدد در جای مناسب خود درج می‌شود. برای لیست‌های کوچک سریع است. (O(n²)"
    ),
    "Merge Sort (مرتب‌سازی ادغامی)": (
        run_merge_sort,
        "🟡 تقسیم و حل: لیست را دو نیم کرده، هر قسمت را مرتب و سپس با هم ادغام می‌کند. همیشه سریع. (O(n log n)"
    ),
    "Selection Sort (مرتب‌سازی انتخابی)": (
        selection_sort,
        "🟠 در هر مرحله کوچک‌ترین عدد را پیدا می‌کند و به ابتدای لیست می‌برد. ساده ولی کند. (O(n²)"
    ),
    "Quick Sort (مرتب‌سازی سریع)": (
        quick_sort,
        "🔴 یک عدد میانی (pivot) انتخاب می‌کند و لیست را به دو قسمت تقسیم می‌کند. در عمل بسیار سریع. (O(n log n)"
    ),
    "Heap Sort (مرتب‌سازی هیپ)": (
        heap_sort,
        "🟣 با ساختار درختی هیپ کار می‌کند. زمان اجرا ثابت و کارایی خوب، ولی ناپایدار. (O(n log n)"
    )
}

# ========== Streamlit UI ==========

st.set_page_config(page_title="مرتب‌سازی هوشمند", layout="centered")

st.title("✨ مقایسه الگوریتم‌های مرتب‌سازی")
st.markdown("🔍 یک الگوریتم انتخاب کنید، لیست عدد وارد کنید، و ببینید چقدر سریع و چطور مرتب می‌شود!")

selected_algo = st.selectbox("🧠 انتخاب الگوریتم:", list(algorithm_details.keys()))

# نمایش توضیح مربوط به الگوریتم انتخابی
_, description = algorithm_details[selected_algo]
st.markdown(f"ℹ️ **درباره الگوریتم:** {description}")

# ورودی کاربر
input_str = st.text_input("🧮 لیست اعداد (با فاصله):", "5 2 8 3 1")

# دکمه اجرا
if st.button("🚀 مرتب کن"):
    try:
        numbers = list(map(int, input_str.strip().split()))
        arr_copy = numbers.copy()

        # اجرا و زمان‌سنجی
        func, _ = algorithm_details[selected_algo]
        start = time.time()
        sorted_arr = func(arr_copy)
        end = time.time()

        # نتایج
        st.success("✅ مرتب‌سازی با موفقیت انجام شد!")
        st.write("📥 ورودی:", numbers)
        st.write("📤 خروجی:", sorted_arr)
        st.write(f"⏱ زمان اجرا: `{end - start:.6f}` ثانیه")
    except:
        st.error("❌ لطفاً فقط اعداد صحیح وارد کنید.")
############################################################################################################
import random
import matplotlib.pyplot as plt

st.markdown("---")
st.subheader("📊 مقایسه زمان اجرای همه الگوریتم‌ها")

sample_size = st.slider("📦 تعداد اعداد تصادفی:", min_value=10, max_value=2000, value=500, step=10)

if st.button("📈 رسم نمودار مقایسه‌ای"):
    random_data = [random.randint(1, 10000) for _ in range(sample_size)]

    execution_times = {}

    for name, (func, _) in algorithm_details.items():
        data_copy = random_data.copy()

        # برای quick sort چون بازگشتی است، نیاز به اختصاص خروجی داریم
        start = time.time()
        result = func(data_copy)
        end = time.time()

        execution_times[name] = end - start

    # 📊 رسم نمودار
    fig, ax = plt.subplots()
    names = list(execution_times.keys())
    times = list(execution_times.values())

    ax.barh(names, times, color='skyblue')
    ax.set_xlabel("⏱ زمان (ثانیه)")
    ax.set_title(f"مقایسه الگوریتم‌ها برای لیست {sample_size} عددی")

    st.pyplot(fig)
