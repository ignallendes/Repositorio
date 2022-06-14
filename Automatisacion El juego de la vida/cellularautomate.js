class CellularAutomata{

    constructor(size, ctx){
        this.size = size;
        this.ctx = ctx;
        this.cells = [];
    }

    create(){
        for(let x=0; x<this.size; x++){
            let row = [];
            for(let y=0; y<this.size; y++){
                const alive= Math.random()<0.5;
                row.push(alive);
            }
            
            this.cells.push(row);
        }     
    }

    next(){
        this.print();
        this.evaluate();
    }
    print(){
        this.ctx.clearRect(0,0, this.size, this.size);
        for(let x=0; x<this.size; x++){
            for(let y=0; y<this.size; y++){
                if(this.cells[x][y])
                    this.ctx.fillStyle="black";
                else
                    this.ctx.fillStyle="white"

                this.ctx.fillRect(x, y, 1,1);
            }
        }

    }
    evaluate(){
        let cellsAux = 
            new Array(100).fill("").map(()=>new Array(100).fill(false));
        for(let x=0; x<this.size; x++){
            for(let y=0; y<this.size; y++){
                let livingNeighbor = 0;
            }
        }
    }

}

const ctx = cavas.getContext('2d');
const celullarAutomata = 
    new CellularAutomata(100, ctx)
celullarAutomata.create();
celullarAutomata.print();