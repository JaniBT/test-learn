export const perimeter = (param, params) => {
    if (params.length === 0) {
        return param * 4;
    }
    if (params.length === 1) {
        return (param * 2) + (params[0] * 2);
    }
    for (const para of params) {
        param += para
    }
    return param
}