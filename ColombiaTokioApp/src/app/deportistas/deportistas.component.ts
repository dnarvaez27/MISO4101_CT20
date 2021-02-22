import { Component, OnInit } from '@angular/core';
import { Deportista } from '../deportista';
import { DeportistaService } from '../deportista.service';

@Component({
  selector: 'app-deportistas',
  templateUrl: './deportistas.component.html',
  styleUrls: ['./deportistas.component.css']
})
export class DeportistasComponent implements OnInit {

  deportistas: Deportista[];

  selectedDeportista: Deportista;

  constructor(private deportistaService: DeportistaService) { }

  ngOnInit(): void {
    this.getDeportistas();
  }

  onSelect(deportista: Deportista): void {
    this.selectedDeportista = deportista;
  }

  getDeportistas(): void{
    this.deportistaService.getDeportistas().subscribe(deportistas => this.deportistas = deportistas);
  }

}
