export function checkInput(input: HTMLInputElement): void {
    if (input.value.length >= 8 && input.value !== "") {
        input.classList.add("green-border");
    } else {
        input.classList.remove("green-border");
        input.classList.add("red-border");
    }
}

export function styleRemover(element: HTMLElement) {
    element.classList.remove("red", "green", "green-border", "red-border")
}

export function swapClasses(element: HTMLElement, removeClass: string, addClass: string) {
    element.classList.remove(removeClass)
    element.classList.add(addClass)
}


export async function postData(url: string, data: any) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    console.log(response);

    // Object
    console.log(result);
    return result;
}

export function clearInputs(inputs: HTMLInputElement[]) {
    for (const input of inputs) {
        input.value = ""
    }
}