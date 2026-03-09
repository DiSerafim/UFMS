// Criar classe Subject.
class DataSubject {
    constructor () {
        this.observers = [];
        this.data = null;
    }

    // Inscreve os observer
    addObserver(observer) {
        this.observers.push(observer);
    }

    // Notifica os observer
    notifyObservers() {
        this.observers.forEach(
            observer => observer.update(this.data)
        );
    }

    // Atualiza os dados e notifica os observer
    setData(newData) {
        this.data = newData;
        this.notifyObservers();
    }
};

// Crie a classe Observer.
class DataPanel {
    update(data) {
        console.log("Painel atualizado com dados novos, ", data);
    }
};

// Exemplo de uso
const dataSubject = new DataSubject();
const panel1 = new DataPanel();
const panel2 = new DataPanel();

dataSubject.addObserver(panel1);
dataSubject.addObserver(panel2);

// Saída
dataSubject.setData("Serafim");