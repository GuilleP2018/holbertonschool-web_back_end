export default class Building {
  constructor(sqft) {
    if (this.constructor === Building){
      throw new TypeError('Cannot instatiate from Building directly');
    }
    if (this.evacuationWarningMessage === undefined){
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
