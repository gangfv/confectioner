let offset = 0;

const width = document.querySelector('.slider-line').children[0].clientWidth
const maxOffset = document.querySelector('.slider-line').children.length
const renderOffset = () => {
    document.querySelector('.slider-line').style.left = `${width * offset}px`
}

$('#next').click(() => {
    if (offset > -(maxOffset - 1)) {
        offset -= 1

    } else {
        offset = 0
    }

    renderOffset()

})

$('#prev').click(() => {
    if (offset < 0) {
        offset += 1

    } else {
        offset = -(maxOffset - 1)
    }


    renderOffset()

})