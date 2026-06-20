//import { Member } from './Member';

export class Opinion {
  private _opinion_id: number = 0;
  private _description: string = '';
  // private _members: Array<Member> = [];

  // on ne peut avoir un seul constructeur en angular
  /*
  constructor(data: any) {
    data.opinion_id
      ? (this._opinion_id = data.opinion_id)
      : (this._opinion_id = 0);
  }
              autre ecriture
  constructor(opinion_id: number, description: string, members: Array<Member>) {
    this._opinion_id = opinion_id;
    this._description = description;
    //this.members = members;
  }*/

  //on fait generlement un type any , any veut que cela peut etre n'importe quoi
  // on ne sait ce c'est a l'avance
  //ici on a l'assurance avec le Back-End que l'on aura un retour de l'opinion
  //nous a l'avance on sait que l'on des elememts.on peut ecrire ce suit ci-dessous
  constructor(data: any) {
    this._opinion_id = data.opinion_id;
    this._description = data.description;
    //this.members = data.members;
  }
  // Getter et Setter pour opinion_id
  public get opinion_id(): number {
    return this._opinion_id;
  }
  public set opinion_id(value: number) {
    this._opinion_id = value;
  }

  // Getter et Setter pour description
  public get description(): string {
    return this._description;
  }
  public set description(value: string) {
    this._description = value;
  }

  // Getter et Setter pour members
  /*
  public get members(): Array<Member> {
    return this._members;
  }
  public set members(value: Array<Member>) {
    this._members = value;
  }*/
}
