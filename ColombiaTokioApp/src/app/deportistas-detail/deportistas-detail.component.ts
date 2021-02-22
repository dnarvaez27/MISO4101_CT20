import { Component, OnInit, Input } from '@angular/core';
import { Deportista } from '../deportista';

@Component({
  selector: 'app-deportistas-detail',
  templateUrl: './deportistas-detail.component.html',
  styleUrls: ['./deportistas-detail.component.css']
})
export class DeportistasDetailComponent implements OnInit {

  @Input() deportista: Deportista;

  constructor() { }

  ngOnInit(): void {
  }

}
