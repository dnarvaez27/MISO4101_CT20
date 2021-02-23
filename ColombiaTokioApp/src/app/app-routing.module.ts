import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DeportistasComponent} from './deportistas/deportistas.component'

const routes: Routes = [
  { path: 'deportistas', component: DeportistasComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
