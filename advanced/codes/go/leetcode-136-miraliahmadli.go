func singleNumber(nums []int) int {
    var res = 0
    for _, element := range nums{
        res = res^element
    }
    return res
}