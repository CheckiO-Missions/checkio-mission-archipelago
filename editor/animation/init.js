requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function archipelagoVisualization(tgt_node, data) {
            if (!data || !data.ext) {
                return
            }

            /**
             * 
             * attr
             * 
             */
            const attr = {
                island: {
                    number: {
                        'font-family': 'times',
                        'fill': '#FFFFFF',
                    },
                    land: {
                        'fill': '#006CA9',
                        'stroke': '#006CA9',
                        'stroke-linecap': 'round',
                        'stroke-linejoin': 'round',
                        'stroke-width': '40px',
                    },
                },
                grid: {
                    'stroke-width': '1px',
                    'stroke': '#82D1F5',
                    'stroke': '#65A1CF',
                },
                bridge: {
                    correct: {
                        'fill': '#F4A561',
                        'stroke': '#F7C091',
                        'stroke': '#333333',
                        'stroke-width': '.5px',
                    },
                    error: {
                        'fill': '#82D1F5',
                        'stroke': '#F7C091',
                        'stroke': '#333333',
                        'stroke-width': '.5px',
                    },
                },
                bottom_text: {
                    'font-family': 'times',
                    'font-size': '10px',
                },
                top_text: {
                    'font-family': 'times',
                    'font-size': '13px',
                    'fill': '#666666',
                    'stroke-width': '0px',
                },

            }

            /**
             * 
             * values
             * 
             */
            const input = data.in[0].values
            const output = data.out.values
            const explanation = data.ext.explanation
            const correct = data.out_ext.correct
            const margin = 10
            const margin_top = 22
            const margin_bottom = 20
            const draw_area_edge_max = 190
            const w = input[0].values.length
            const h = input.length
            const grid_edge = draw_area_edge_max / Math.max(w, h)
            const draw_area_edge_w = grid_edge * w
            const draw_area_edge_h = grid_edge * h
            const scale = 5 / Math.max(w, h)
            const islands_coord = {}
            const islands_obj = []
            let state = 0

            /**
             * 
             * paper
             * 
             */
            const paper = Raphael(tgt_node,
                draw_area_edge_w + margin * 2,
                draw_area_edge_h + margin_top + margin_bottom)

            /**
             * 
             * get random int
             * 
             */
            function get_random_int(max) {
                return Math.floor(Math.random() * max)
            }

            /**
             * 
             * draw island
             * 
             */
            function draw_island(ix, iy, number) {
                const ps = paper.set()
                const ps2 = paper.set()
                ps.push(paper.rect(
                    margin + grid_edge * (ix + .2),
                    margin_top + grid_edge * (iy + .2),
                    grid_edge * .6,
                    grid_edge * .6,
                ).attr(attr.island.land)).attr({ 'stroke-width': 8 * scale + 'px' })
                ps2.push(paper.text(
                    margin + grid_edge * (ix + .5),
                    margin_top + grid_edge * (iy + .5), number)
                ).attr(attr.island.number).attr({ 'font-size': 20 * scale + 'px' })
                return ps, ps2
            }

            /**
             *
             * draw islands
             *
             */
            function draw_islands(state) {
                let island_num = 0
                for (let y = 0; y < h; y += 1) {
                    for (let x = 0; x < w; x += 1) {
                        if (input[y].values[x] != 0) {
                            if (state) {
                                islands_obj.push(draw_island(x, y, input[y].values[x]))
                            } else {
                                island_num += 1
                                islands_obj.push(draw_island(x, y, island_num))
                            }
                            islands_coord[island_num] = [y, x]
                        }
                    }
                }
            }

            /**
             * 
             * draw bridge
             * 
             */
            function draw_bridge(source, destination, num) {
                const [sy, sx] = islands_coord[source]
                const [dy, dx] = islands_coord[destination]
                // horizontal
                if (sy == dy) {
                    for (let n = 0; n < num; n += 1) {
                        let bg = paper.rect(
                            margin + grid_edge * (Math.min(sx, dx) + .5),
                            margin_top + grid_edge * (sy + ((7 - (num - 1)) / 8 / 2) + n / 8),
                            Math.abs(sx - dx) * grid_edge,
                            grid_edge / 8
                        ).attr(correct ? attr.bridge.correct : attr.bridge.error)
                        bg.toBack()
                    }
                    // vertical
                } else {
                    for (let n = 0; n < num; n += 1) {
                        let bg = paper.rect(
                            margin + grid_edge * (sx + ((7 - (num - 1)) / 8 / 2) + n / 8),
                            margin_top + grid_edge * (Math.min(sy, dy) + .5),
                            grid_edge / 8,
                            Math.abs(sy - dy) * grid_edge
                        ).attr(correct ? attr.bridge.correct : attr.bridge.error)
                        bg.toBack()
                    }
                }
            }

            /**
             * 
             * main
             * 
             */
            // draw grid
            for (y = 0; y <= h; y += 1) {
                paper.path(['M', margin, margin_top + y * grid_edge, 'h', grid_edge * w]).attr(
                    attr.grid).attr({ 'stroke-width': scale + 'px' })
            }
            for (x = 0; x <= w; x += 1) {
                paper.path(['M', margin + x * grid_edge, margin_top, 'v', grid_edge * h]).attr(
                    attr.grid).attr({ 'stroke-width': scale + 'px' })
            }
            // init draw islands
            draw_islands(state)
            // click event
            tgt_node.onclick = function () {
                islands_obj.forEach(i => {
                    i.remove()
                })
                state = 1 - state
                draw_islands(state)
                return false
            }
            // draw explanation text
            paper.text((margin * 2 + draw_area_edge_w) / 2,
                margin_top / 2, explanation).attr(attr.top_text)
            // draw bottom text
            paper.text((margin * 2 + draw_area_edge_w) / 2,
                margin_top + draw_area_edge_h + margin_bottom / 2,
                'Click anywhere to change the numbers').attr(attr.bottom_text)
            // check answer
            if (toString.call(output) !== '[object Array]') {
                return
            }
            for (let i = 0; i < output.length; i += 1) {
                if (toString.call(output[i].values) !== '[object Array]') {
                    return
                }
                if (output[i].values.length !== 3) {
                    return
                }
                for (let j = 0; j < output[i].values.length; j += 1) {
                    if (toString.call(output[i].values[j]) !== '[object Number]') {
                        return
                    }
                    let [island_01, island_02, bridge_num] = output[i].values
                    if (!island_01 in islands_coord) {
                        return
                    }
                    if (!island_02 in islands_coord) {
                        return
                    }
                    const [sy, sx] = islands_coord[island_01]
                    const [dy, dx] = islands_coord[island_02]
                    if (sy != dy && sx != dx) {
                        return
                    }
                    if (!(bridge_num == 1 || bridge_num == 2)) {
                        return
                    }
                }
            }
            // draw bridges
            output.forEach(brides => {
                draw_bridge(...brides.values)
            })
        }
        var io = new extIO({
            animation: function ($expl, data) {
                archipelagoVisualization(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
